from vpython import *
import time
import config

# 创建一个文本标签用于显示运行时间
time_label = label(
    pos=vector(-24, 20, 0),  # 标签的位置
    text="Time: 0.0s",  # 初始文本
    xoffset=1,  # 文本的X偏移量
    yoffset=1,  # 文本的Y偏移量
    height=15,  # 字体高度
    border=3,  # 标签边框宽度
    font='sans',  # 字体类型
    color=color.black  # 字体颜色
)

def record_time(current_time):
    time_label.text = f"Time: {current_time:.1f}s"


