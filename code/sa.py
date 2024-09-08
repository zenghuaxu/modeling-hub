import numpy as np
import random as rd
import math

import config
from q4 import t_to_xy_q4
from calculate import find_delta_time, list_cartesian_distance

right =18.0
left  =9.0
alpha =0.95
T     =4.0
initial_t = (right + left) / 2
iteration = 5 # 每个温度下迭代次数
node_num = 10 # 默认只计算前十节的最大速度以加快计算

def next_time(x):
    x_next = x + T * 2 * (rd.random()-0.5)
    if x_next < left:
        temp = rd.random()
        return temp*left+(1-temp)*x
    elif x_next > left and x_next <= right:
        return x_next
    else:
        temp = rd.random()
        return temp*right+(1-temp)*x


def evaluate_function(t, dt=1e-5, node_num=node_num):
    # print(f"maximum velocity at {t:.6f}s is...", end='')
    dis_tolerance = 1e-12
    vmax = 0
    index_max: int
    
    x, y = t_to_xy_q4(t)
    _x, _y = t_to_xy_q4(t - dt)
    ds = list_cartesian_distance([x, y], [_x, _y])
    v = ds / dt
    
    if v > vmax:
        vmax = v
        index_max = 0

    # 更新接下来的点的位置
    ergodic_time = t
    _ergodic_time = t - dt
    for i in range(1, 11):
        delta_time = find_delta_time(ergodic_time, config.actual_fixed_distances[0 if i == 1 else 1], dis_tolerance)
        ergodic_time -= delta_time
        x, y = t_to_xy_q4(ergodic_time)
        _delta_time = find_delta_time(_ergodic_time, config.actual_fixed_distances[0 if i == 1 else 1], dis_tolerance)
        _ergodic_time -= _delta_time
        _x, _y = t_to_xy_q4(_ergodic_time)
        ds = list_cartesian_distance([x, y], [_x, _y])
        v = ds / dt
    
        if v > vmax:
            vmax = v
            index_max = i
    # print(f"{vmax:.6f}m/s")
    return vmax, i


# 使用 Metropolis 算法计算概率
def p(t, t_next):
    return math.exp(-abs(evaluate_function(t)[0]-evaluate_function(t_next)[0])/(T * 0.01))

def sa():
    global T
    time_tolerance = 1e-5
    rd.seed(1234)
    t = initial_t
    iter = 0
    total_iter = int(np.log(time_tolerance / T) / np.log(alpha))
    f_t, index_t = evaluate_function(t)
    print(index_t.__class__)
    f_next: float
    while T > time_tolerance:
        iter += 1
        print(f"\033[32mRound ({iter}/{total_iter}): {f_t:.6f}m/s at {t:.6f}s when T={T:.06f}\033[0m")
        for i in range(iteration):
            t_next = next_time(t)
            f_t, index_t = evaluate_function(t)
            f_next, index_next = evaluate_function(t_next)
            if f_next >= f_t:
                print(f"{f_next:.6f}m/s at {t_next:.06f}s is faster and accpected")
                t = t_next
                index_t = index_next
            elif rd.random() <= p(t, t_next):
                print(f"{f_next:.6f}m/s at {t_next:.06f}s is ramdomly accepted")
                t = t_next
                index_t = index_next
        T *= alpha
    print(f'最大值为：{evaluate_function(t)[0]:.6f}m/s, 最大值点为：{t}s, 把手号为：{index_t}')

