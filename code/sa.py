#本功能实现最小值的求解#

from matplotlib import pyplot as plt
import numpy as np
import random
import math

import config
from q4 import t_to_xy_q4
from calculate import find_delta_time, list_cartesian_distance
plt.ion()#这里需要把matplotlib改为交互状态

#初始值设定
hi=20
lo=-1
alf=0.95
T=0.1

#目标函数
def f(t, dt=1e-5, node_num=10):
    print(f"maximum velocity at {t:.6f}s is...", end='')
    vmax = 0
    
    x, y = t_to_xy_q4(t)
    _x, _y = t_to_xy_q4(t - dt)
    ds = list_cartesian_distance([x, y], [_x, _y])
    v = ds / dt
    
    vmax = v if v > vmax else vmax

    # 更新接下来的点的位置
    ergodic_time = t
    _ergodic_time = t - dt
    for i in range(1, 11):
        delta_time = find_delta_time(ergodic_time, config.actual_fixed_distances[0 if i == 1 else 1])
        ergodic_time -= delta_time
        x, y = t_to_xy_q4(ergodic_time)
        _delta_time = find_delta_time(_ergodic_time, config.actual_fixed_distances[0 if i == 1 else 1])
        _ergodic_time -= _delta_time
        _x, _y = t_to_xy_q4(_ergodic_time)
        ds = list_cartesian_distance([x, y], [_x, _y])
        v = ds / dt
        
        vmax = v if v > vmax else vmax
    print(f"{vmax:.6f}m/s")
    return -vmax
    

#可视化函数（开始清楚一次然后重复的画）
def visual(x):
    plt.cla()
    plt.axis([lo-1,hi+1,-20,20])
    m=np.arange(lo,hi,0.0001)
    # plt.plot(m,f(m))
    # plt.plot(x,f(x),marker='o',color='black',markersize='4')
    plt.title('temperature={}'.format(T))
    plt.pause(0.1)#如果不停啥都看不见

#随机产生初始值
def init():
    return 14.5

#新解的随机产生
def new(x):
    x1=x+T*random.uniform(-1,1)
    if (x1<=hi)&(x1>=lo):
        return x1
    elif x1<lo:
        rand=random.uniform(-1,1)
        return rand*lo+(1-rand)*x
    else:
        rand=random.uniform(-1,1)
        return rand*hi+(1-rand)*x

#p函数
def p(x,x1):
    return math.exp(-abs(f(x)-f(x1))/(T * 0.01))

def main():
    global x
    global T
    x=init()
    while T>0.0001:
        # visual(x)
        print(f"t = {x:.6f}s at Tempreture {T}")
        for i in range(5):
            x1=new(x)
            # print(f"checking position {x1}")
            if f(x1)<=f(x):
                print(f"{x1:.06f} is better and accpected")
                x=x1
            elif random.random()<=p(x,x1):
                print(f"{x1:.06f} is ramdomly accepted")
                x=x1
        T=T*alf
    print(f'最大值为：{-f(x)}, 最大值点为：{x}')

if __name__ == "__main__":
    main()
