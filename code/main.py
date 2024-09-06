from vpython import *
import generate
import numpy as np

# 初始设置
scene.background = color.white
x_axis = arrow(pos=vector(-30, 0, 0), axis=vector(60, 0, 0), shaftwidth=0.05, color=color.black)
y_axis = arrow(pos=vector(0, -30, 0), axis=vector(0, 60, 0), shaftwidth=0.05, color=color.black)

# 绘制板凳龙
# 把手
points = [sphere(pos=vector(0, 0, 0), radius=0.2, color=color.black) for _ in range(224)]

# 把手连线
lines = [curve(color=color.black, radius=0.03) for _ in range(223)]

# 龙头前把手与后把手的间距
# 龙身与龙尾前把手与后把手的间距
fixed_distances = [0.4 * np.pi * 286 / 55, 0.4 * np.pi * 165 / 55]

if __name__ == "__main__":
    generate.generate_spiral()
    generate.generate(points, lines, fixed_distances)