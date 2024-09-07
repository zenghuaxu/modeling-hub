from calculate import *
from info import *
from cross import cal_long_side

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

def generate_bench_line(bench_lines, positions):
    # 消除之前的连线
    for i in range(0, len(bench_lines)):
        for j in range(0, len(bench_lines[i])):
            bench_lines[i][j].clear()

    # 依次连接把手
    for i in range(0, len(positions) - 1):
        font_in, back_in, font_out, back_out = (
            cal_long_side(np.array([positions[i].x, positions[i].y]), np.array([positions[i + 1].x, positions[i + 1].y]), True if i == 0 else False))
        bench_lines[0][i].append(vector(font_in[0], font_in[1], 0))
        bench_lines[0][i].append(vector(font_out[0], font_out[1], 0))
        bench_lines[1][i].append(vector(back_in[0], back_in[1], 0))
        bench_lines[1][i].append(vector(back_out[0], back_out[1], 0))
        bench_lines[2][i].append(vector(font_in[0], font_in[1], 0))
        bench_lines[2][i].append(vector(back_in[0], back_in[1], 0))
        bench_lines[3][i].append(vector(font_out[0], font_out[1], 0))
        bench_lines[3][i].append(vector(back_out[0], back_out[1], 0))
    
def generate_spiral():
    spiral = curve(color=color.black, radius=0.05)

    # 创建关键点
    theta = 0
    while theta < config.theta_max:
        r = config._spacing * theta
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        spiral.append(vector(x, y, 0))
        theta += 0.01

def generate(points, lines, bench_lines):
    current_time = time.time() - config.start_time
    theta = t_to_theta(current_time)
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
            delta_theta = find_delta_theta(current_theta, config.fixed_distances[0 if i == 1 else 1])
            pos = get_position(current_theta + delta_theta)
            positions.append(pos)
            points[i].pos = pos
            current_theta += delta_theta

        # 更新连线
        generate_line(lines, positions)
        generate_bench_line(bench_lines, positions)

        # 更新角度，继续移动
        theta -= 0.05  # 控制第一个点的移动速度

        if theta < 0:
            config.start_time = time.time() - 350.0

        current_time = time.time() - config.start_time
        theta = t_to_theta(current_time)
        
