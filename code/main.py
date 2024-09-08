from gen_xlsx import *
from sa import *
from cross import *
from trisection import *

import generate
import config

if __name__ == "__main__":
    print("请打开当前目录下的main.py文件，根据注释运行各问代码，查看输出结果")
    # 未运行倒数两个可视化代码会弹出仅有坐标系和时间标签的网页，请关闭后继续查看标准输出框的结果
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
    # local_check()

    # 第四问数据生成
    # 以调头开始时间为零时刻，从 −100s 开始到 100s 为止，每秒舞龙队的位置，储存在当前目录下的result4_dis.xlsx中
    # q4_dis_xlsx_init()
    # q4_dis_fill()

    # 以调头开始时间为零时刻，从 −100s 开始到 100s 为止，每秒舞龙队的速度，储存在当前目录下的result4_v.xlsx中
    # q4_v_xlsx_init()
    # q4_v_fill()

    # 第五问验证算法
    # 模拟退火算法
    # sa()
    # 三分算法
    # print(f"{trisection_max(f)}")

    # 网页弹出后，网页部分内容为黑色，表明正在加载，请稍等片刻后，等待图像基本加载完毕，使用鼠标拖动边框或在可视化界面中滑动滚轮调节图像大小
    # 第一问可视化
    # generate.q1_generate_spiral()
    # generate.q1_generate(points, lines, bench_lines)

    # 第四问可视化
    # generate.q4_generate_curve()
    # generate.q4_generate(points, lines, bench_lines)


