from vpython import *
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
    generate.q1_generate_spiral()
    generate.q1_generate(points, lines, bench_lines)
    # generate.q4_generate_curve()
    # generate.q4_generate(points, lines, bench_lines)
