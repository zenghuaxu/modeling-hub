import time

import numpy as np

# 绘制等距螺线
# 参数设置
spacing = 0.2  # 控制螺线的间距
theta_max = 32 * np.pi  # 控制螺线的最大角度
fixed_distances = [0.4 * np.pi * 286 / 55, 0.4 * np.pi * 165 / 55]   # 龙头前把手与后把手的间距 + 龙身与龙尾前把手与后把手的间距
actual_fixed_distances = [286, 165]   # 龙头前把手与后把手的间距 + 龙身与龙尾前把手与后把手的间距
sys_length = 30
start_time = time.time()
integer_time = 0

dis_tolerance = 1e-6
time_tolerance = 1e-5
