#本功能实现最小值的求解#

from matplotlib import pyplot as plt
import numpy as np
import random
import math

import config
from q4 import t_to_xy_q4
from calculate import find_delta_time, list_cartesian_distance
plt.ion()#这里需要把matplotlib改为交互状态

#初始值设定
hi=18
lo=9
alf=0.95
T=0.1

#目标函数
def f(t, dt=1e-5, node_num=10):
    print(f"maximum velocity at {t:.6f}s is...", end='')
    vmax = 0
    
    x, y = t_to_xy_q4(t)
    _x, _y = t_to_xy_q4(t - dt)
    ds = list_cartesian_distance([x, y], [_x, _y])
    v = ds / dt
    
    vmax = v if v > vmax else vmax

    # 更新接下来的点的位置
    ergodic_time = t
    _ergodic_time = t - dt
    for i in range(1, node_num+1):
        delta_time = find_delta_time(ergodic_time, config.actual_fixed_distances[0 if i == 1 else 1])
        ergodic_time -= delta_time
        x, y = t_to_xy_q4(ergodic_time)
        _delta_time = find_delta_time(_ergodic_time, config.actual_fixed_distances[0 if i == 1 else 1])
        _ergodic_time -= _delta_time
        _x, _y = t_to_xy_q4(_ergodic_time)
        ds = list_cartesian_distance([x, y], [_x, _y])
        v = ds / dt
        
        vmax = v if v > vmax else vmax
    print(f"{vmax:.6f}m/s")
    return vmax

def trisection_max(f, lo=lo, hi=hi):
    l = float(lo)
    r = float(hi)
    lmid = 2.0/3*l + 1/3 * r
    rmid = 1.0/3*l + 2/3 * r
    print(f"lmid = {lmid:.6f}, rmid = {rmid:.6f}")
    
    while (r-l >= 1e-7):
        fl = f(lmid)
        fr = f(rmid)
        print(f"fl = {fl} >= fr = {fr}")
        if (fl > fr):
            r = rmid
            lmid = 2.0/3*l + 1/3 * r
            rmid = 1.0/3*l + 2/3 * r
        else:
            l = lmid
            lmid = 2.0/3*l + 1/3 * r
            rmid = 1.0/3*l + 2/3 * r
        print(f"lmid = {lmid:.6f}, rmid = {rmid:.6f}")
        print(f"l = {l:.6f}, r = {r:.6f}")
    return (l+r)/2

if __name__ == '__main__':
    print(f"{trisection_max(f)}")