from calculate import *
from info import *

import time
import numpy as np
import config

def generate_line(lines, positions):
    # 消除之前的连线
    for i in range(0, len(lines)):
        lines[i].clear()

    # 依次连接把手
    for i in range(0, len(lines)):
        lines[i].append(positions[i])
        lines[i].append(positions[i + 1])

    
def generate_spiral():
    spiral = curve(color=color.black, radius=0.05)

    # 创建关键点
    theta = 0
    while theta < config.theta_max:
        r = config.spacing * theta
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        spiral.append(vector(x, y, 0))
        theta += 0.01

def generate(points, lines, fixed_distances):
    # 龙头起始位置
    theta = 20 * np.pi
    while theta > 0:
        rate(60)  # 控制移动速度
        record_time()

        # 更新第一个点的位置
        pos_1 = get_position(theta)
        points[0].pos = pos_1

        # 更新接下来的点的位置
        current_theta = theta
        positions = [pos_1]
        for i in range(1, len(points)):
            delta_theta = find_delta_theta(current_theta, fixed_distances[0 if i == 1 else 1])
            pos = get_position(current_theta + delta_theta)
            positions.append(pos)
            points[i].pos = pos
            current_theta += delta_theta

        # 更新连线
        generate_line(lines, positions)

        # 更新角度，继续移动
        theta -= 0.05  # 控制第一个点的移动速度

        if theta < 0:
            theta = 20 * np.pi
            config.start_time = time.time()
        
