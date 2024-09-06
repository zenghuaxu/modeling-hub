from vpython import *
import generate
import config

# 初始设置
scene.background = color.white
x_axis = arrow(pos=vector(-config.sys_length, 0, 0), axis=vector(2 * config.sys_length, 0, 0), shaftwidth=0.05, color=color.black)
y_axis = arrow(pos=vector(0, -config.sys_length, 0), axis=vector(0, 2 * config.sys_length, 0), shaftwidth=0.05, color=color.black)

# 绘制板凳龙
# 把手
points = [sphere(pos=vector(0, 0, 0), radius=0.2, color=color.black) for _ in range(224)]

# 把手连线
lines = [curve(color=color.black, radius=0.03) for _ in range(223)]

if __name__ == "__main__":
    generate.generate_spiral()
    generate.generate(points, lines, config.fixed_distances)
