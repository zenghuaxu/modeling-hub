from vpython import *
from q4 import *
from scipy.optimize import fsolve

import math
import numpy as np
import config

# 函数
# 根据theta计算螺线上点的位置
def get_position(theta):
    r = config._spacing * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return vector(x, y, 0)

# 计算两点之间的距离
def cartesian_distance(pos1, pos2):
    return np.sqrt((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2)

# 优化
def polar_distance(theta_1, theta_2):
    rho_1 = config._spacing * theta_1
    rho_2 = config._spacing * theta_2
    return np.sqrt(rho_1 ** 2 + rho_2 ** 2 - 2 * rho_1 * rho_2 * np.cos(theta_1 - theta_2))

# 使用二分法寻找更准确的 delta_theta
def find_delta_theta(theta, fixed_distance):
    # 二分上下限
    low = 0
    high = np.pi - 1e-2
    while high - low > config.dis_tolerance:
        mid = (low + high) / 2
        pos1 = get_position(theta)
        pos2 = get_position(theta + mid)
        dist = cartesian_distance(pos1, pos2)
        # dist = polar_distance(theta, theta + mid)
        if dist < fixed_distance:
            low = mid
        else:
            high = mid
    return (low + high) / 2

def find_delta_time(time, fixed_distance):
    low = 1.5
    high = 6
    while high - low > config.dis_tolerance:
        mid = (low + high) / 2
        x1, y1 = t_to_xy_q4(time)
        x2, y2 = t_to_xy_q4(time - mid)
        x1, y1 = x1 * 100, y1 * 100
        x2, y2 = x2 * 100, y2 * 100
        dist = list_cartesian_distance([x1, y1], [x2, y2])
        # dist = polar_distance(theta, theta + mid)
        if dist < fixed_distance:
            low = mid
        else:
            high = mid
    return (low + high) / 2

def list_cartesian_distance(pos1, pos2):
    return float(np.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2))

def get_actual_position(theta, space):
    r = config._spacing * theta
    x = r * np.cos(theta) / (2 * config._spacing * np.pi) * space
    y = r * np.sin(theta) / (2 * config._spacing * np.pi) * space
    return [x, y]

def find_actual_delta_theta(theta, fixed_distance, space):
    # 二分上下限
    low = 0
    high = 4
    while high - low > config.dis_tolerance:
        mid = (low + high) / 2
        pos1 = get_actual_position(theta, space)
        pos2 = get_actual_position(theta + mid, space)
        dist = list_cartesian_distance(pos1, pos2)
        # dist = polar_distance(theta, theta + mid)
        if dist < fixed_distance:
            low = mid
        else:
            high = mid
    return (low + high) / 2

# 需要已知的参数 t 来求解 theta
def theta_t(theta):
    return -1/2 * np.log(np.sqrt(1 + theta**2) - theta) + 1/2 * theta * np.sqrt(theta ** 2 + 1)

D_q1 = 0.55 # 螺距 m
v_q1 = 1 # 龙头速度 m/s
C_q1 = theta_t(32 * math.pi) * D_q1 / (2*math.pi) # 积分常数，不要动

def equ(theta, t, D, v, C):
    return - theta_t(theta) * D / (2 * math.pi) - v * t + C

def t_to_theta(t, D=D_q1, v=v_q1, C=C_q1):
    initial = 0.0
    return fsolve(equ, initial, args=(t, D, v, C))

def t_to_dis(t, space):
    positions = np.empty((224, 2))
    theta = t_to_theta(t)
    pos = get_actual_position(theta, space)
    x = pos[0][0] / 100.0
    y = pos[1][0] / 100.0
    positions[0] = np.array([x, y])

    current_theta = theta
    for i in range(1, 224):
        delta_theta = find_actual_delta_theta(current_theta, config.actual_fixed_distances[0 if i == 1 else 1], space)
        current_theta += delta_theta
        pos = get_actual_position(current_theta, space)
        x = pos[0][0] / 100.0
        y = pos[1][0] / 100.0
        positions[i] = np.array([x, y])

    return positions
