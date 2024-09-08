from gen_xlsx import *

import generate
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


if __name__ == "__main__":
    # 第一问数据生成
    # 初始时刻到 300s 为止，每秒整个舞龙队的位置，储存在当前目录下的result1_dis.xlsx中
    # dis_xlsx_init()
    # dis_fill_xlsx()

    # 初始时刻到 300s 为止，每秒整个舞龙队的速度，储存在当前目录下的result1_v.xlsx中
    # v_xlsx_init()
    # v_fill_xlsx()

    # 第二问数据生成
    # 舞龙队盘入恰好使得板凳之间不发生碰撞的时刻下舞龙队的位置和速度，储存在当前目录下的result2.xlsx中
    # collision_xlsx_init()
    # collision_fill_xlsx()

    # 第三问验证函数
    # pso_cal_min_distance(...)

    # 第四问数据生成
    # 以调头开始时间为零时刻，从 −100s 开始到 100s 为止，每秒舞龙队的位置，储存在当前目录下的result4_dis.xlsx中
    # q4_dis_xlsx_init()
    # q4_dis_fill()

    # 以调头开始时间为零时刻，从 −100s 开始到 100s 为止，每秒舞龙队的速度，储存在当前目录下的result4_v.xlsx中
    # q4_v_xlsx_init()
    # q4_v_fill()

    # 第五问验证函数
    # q5_v_find_test()

    # 第一问可视化
    generate.q1_generate_spiral()
    generate.q1_generate(points, lines, bench_lines)

    # 第四问可视化
    # generate.q4_generate_curve()
    # generate.q4_generate(points, lines, bench_lines)


