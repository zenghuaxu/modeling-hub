from calculate import *
from info import *
from cross import cal_long_side

import time
import numpy as np
import q4
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
    
def q1_generate_spiral():
    spiral = curve(color=color.black, radius=0.05)

    # 创建关键点
    theta = 0
    while theta < config.theta_max:
        r = config._spacing * theta
        x = r * np.cos(theta)
        y = r * np.sin(theta)
        spiral.append(vector(x, y, 0))
        theta += 0.01

def q1_generate(points, lines, bench_lines):
    current_time = time.time() - config.start_time
    theta = t_to_theta(current_time)
    while theta > 0:
        rate(60)  # 控制移动速度
        record_time(current_time)

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

def q4_generate_curve():
    spiral = curve(color=color.black, radius=0.05)

    # 创建关键点
    t = config.q4_start_time
    while t < config.q4_end_time:
        x, y = t_to_xy_q4(t)
        x = x * config.median
        y = y * config.median
        spiral.append(vector(x, y, 0))
        t += 0.01

def q4_generate(points, lines, bench_lines):
    current_time = 380
    end_time = 600
    while current_time < end_time:
        rate(60)  # 控制移动速度
        record_time(current_time)

        # 更新第一个点的位置
        x, y = t_to_xy_q4(current_time)
        x = x * config.median
        y = y * config.median
        pos_1 = vector(x, y, 0)
        points[0].pos = pos_1

        # 更新接下来的点的位置
        ergodic_time = current_time
        positions = [pos_1]
        for i in range(1, len(points)):
            st = time.time()
            delta_time = find_delta_time(ergodic_time, config.actual_fixed_distances[0 if i == 1 else 1])
            et = time.time()
            print("cal:", et - st)
            ergodic_time -= delta_time
            _x, _y = t_to_xy_q4(ergodic_time)
            _x = _x * config.median
            _y = _y * config.median
            pos = vector(_x, _y, 0)
            positions.append(pos)
            points[i].pos = pos

        # 更新连线
        st = time.time()
        generate_line(lines, positions)
        generate_bench_line(bench_lines, positions)
        et = time.time()
        print("draw: ", et - st)

        current_time += 5