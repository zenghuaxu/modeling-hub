from calculate import *
from info import *
from cross import cal_long_side

import time
import numpy as np
import q4
import config

# 初始设置
scene.background = color.white
x_axis = arrow(pos=vector(-config.sys_length, 0, 0), axis=vector(2 * config.sys_length, 0, 0), shaftwidth=0.05, color=color.black)
y_axis = arrow(pos=vector(0, -config.sys_length, 0), axis=vector(0, 2 * config.sys_length, 0), shaftwidth=0.05, color=color.black)

# 绘制板凳龙
# 把手
points = [sphere(pos=vector(0, 0, 0), radius=0.2, color=color.black) for _ in range(config.section_num + 1)]

# 把手连线
lines = [curve(color=color.black, radius=0.03) for _ in range(config.section_num)]

for_bench_line = [curve(color=color.black, radius=0.03) for _ in range(config.section_num + 1)]
beh_bench_line = [curve(color=color.black, radius=0.03) for _ in range(config.section_num + 1)]
left_bench_line = [curve(color=color.black, radius=0.03) for _ in range(config.section_num + 1)]
right_bench_line = [curve(color=color.black, radius=0.03) for _ in range(config.section_num + 1)]
bench_lines = [for_bench_line, beh_bench_line, left_bench_line, right_bench_line]

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
        # 自定义一个多边形顶点列表
        vertices = [
            vector(font_in[0], font_in[1]),  # 顶点 1
            vector(font_out[0], font_out[1]),  # 顶点 2
            vector(back_in[0], back_in[1]),  # 顶点 3
            vector(back_out[0], back_out[1])  # 顶点 4
        ]

        # 通过路径连接这些顶点，形成一个封闭的形状
        path = [vector(0, 0, 0), vector(0, 0, 0.01)]  # 定义路径，给它一个小的厚度

        # 使用 extrusion 来将路径挤压并染色
        extrusion(path=path, shape=vertices, color=color.red)
def q1_generate_spiral():
    config.set_spacing(0.3)
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
    current_time = 0
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
            delta_theta = find_delta_theta(current_theta, config.fixed_distances[0 if i == 1 else 1], 1e-3)
            pos = get_position(current_theta + delta_theta)
            positions.append(pos)
            points[i].pos = pos
            current_theta += delta_theta

        # 更新连线
        generate_line(lines, positions)
        generate_bench_line(bench_lines, positions)

        current_time += 0.1
        theta = t_to_theta(current_time)

def q4_generate_curve():
    config.set_spacing(0.4)
    spiral = curve(color=color.black, radius=0.05)

    # 创建关键点
    t = config.q4_start_time
    while t < config.q4_end_time:
        x, y = t_to_xy_q4(t)
        x = x * config.median
        y = y * config.median
        spiral.append(vector(x, y, 0))
        t += 0.05

def q4_generate(points, lines, bench_lines):
    dis_tolerance = 1e-5
    current_time = 14.8
    end_time = 100
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
            delta_time = find_delta_time(ergodic_time, config.actual_fixed_distances[0 if i == 1 else 1], dis_tolerance)
            ergodic_time -= delta_time
            _x, _y = t_to_xy_q4(ergodic_time)
            _x = _x * config.median
            _y = _y * config.median
            pos = vector(_x, _y, 0)
            positions.append(pos)
            points[i].pos = pos

        # 更新连线
        generate_line(lines, positions)
        generate_bench_line(bench_lines, positions)

        current_time += 1
