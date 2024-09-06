from vpython import *

import numpy as np
import config

# 函数
# 根据theta计算螺线上点的位置
def get_position(theta):
    r = config.spacing * theta
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return vector(x, y, 0)

# 计算两点之间的距离
def cartesian_distance(pos1, pos2):
    return np.sqrt((pos1.x - pos2.x) ** 2 + (pos1.y - pos2.y) ** 2)

# 优化
def polar_distance(theta_1, theta_2):
    rho_1 = config.spacing * theta_1
    rho_2 = config.spacing * theta_2
    return np.sqrt(rho_1 ** 2 + rho_2 ** 2 - 2 * rho_1 * rho_2 * np.cos(theta_1 - theta_2))

# 使用二分法寻找更准确的 delta_theta
def find_delta_theta(theta, fixed_distance):
    # 二分上下限
    low = 0
    high = 4
    while high - low > config.tolerance:
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