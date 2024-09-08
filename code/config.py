import time

import numpy as np

# 绘制等距螺线
# 参数设置
_spacing = 0.2  # 控制螺线显示效果
space = 55  # 控制螺距
len_head = 286  # 龙头长度
len_body = 165  # 龙身长度
section_num = 223  # 龙节数
theta_max = 32 * np.pi  # 控制螺线的最大角度
q4_start_time = -100
q4_end_time = 100

fixed_distances = [2 * _spacing * np.pi * len_head / space, 2 * _spacing * np.pi * len_body / space]   # 龙头前把手与后把手的间距 + 龙身与龙尾前把手与后把手的间距
actual_fixed_distances = [len_head, len_body]   # 龙头前把手与后把手的间距 + 龙身与龙尾前把手与后把手的间距
sys_length = 30
start_time = time.time() - 409
actual_q4_start_time = time.time() + 0
actual_q4_end_time = time.time() - 100.0
integer_time = 0

dis_tolerance = 1e-12
time_tolerance = 1e-5

##################################

# q4
median = 2.5
