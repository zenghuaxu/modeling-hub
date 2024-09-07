from openpyxl import Workbook
from openpyxl.styles import Font
from calculate import *

import config

wb = Workbook()
ws = wb.active
font = Font(name='Times New Roman', size=10)

# 填充行名
dis_row_names = ["龙头x (m)", "龙头y (m)"]

for i in range(1, 222):
    dis_row_names.append(f"第{i}节龙身x (m)")
    dis_row_names.append(f"第{i}节龙身y (m)")

dis_row_names.append("龙尾x (m)")
dis_row_names.append("龙尾y (m)")
dis_row_names.append("龙尾（后）x (m)")
dis_row_names.append("龙尾（后）y (m)")

# 填充行名
v_row_names = ["龙头 (m/s)"]

for i in range(1, 222):
    v_row_names.append(f"第{i}节龙身  (m/s)")

v_row_names.append("龙尾  (m/s)")
v_row_names.append("龙尾（后） (m/s)")

# 填充列名
column_names = [f"{i} s" for i in range(301)]  # 从 0 s 到 21 s


def dis_xlsx_init():
    for row_num, row_name in enumerate(dis_row_names, start=2):
        cell = ws.cell(row=row_num, column=1, value=row_name)
        cell.font = font

    for col_num, col_name in enumerate(column_names, start=2):
        cell = ws.cell(row=1, column=col_num, value=col_name)
        cell.font = font


def dis_fill_xlsx():
    for time in range(301):
        theta = t_to_theta(time)
        pos = get_actual_position(theta, config.space)
        x = pos[0][0] / 100.0
        y = pos[1][0] / 100.0
        cell = ws.cell(row=2, column=time + 2, value=f"{x:.6f}")
        cell.font = font
        cell = ws.cell(row=3, column=time + 2, value=f"{y:.6f}")
        cell.font = font

        # 更新接下来的点的位置
        current_theta = theta
        for i in range(1, 224):
            delta_theta = find_actual_delta_theta(current_theta, config.actual_fixed_distances[0 if i == 1 else 1], config.space)
            current_theta += delta_theta
            pos = get_actual_position(current_theta, config.space)
            x = pos[0][0] / 100.0
            y = pos[1][0] / 100.0
            print(f"{time} {i}")
            cell = ws.cell(row=2 * (i + 1), column=time + 2, value=f"{x:.6f}")
            cell.font = font
            cell = ws.cell(row=2 * (i + 1) + 1, column=time + 2, value=f"{y:.6f}")
            cell.font = font

    wb.save("result1_dis.xlsx")


def v_xlsx_init():
    for row_num, row_name in enumerate(v_row_names, start=2):
        cell = ws.cell(row=row_num, column=1, value=row_name)
        cell.font = font

    for col_num, col_name in enumerate(column_names, start=2):
        cell = ws.cell(row=1, column=col_num, value=col_name)
        cell.font = font


def v_fill_xlsx():
    for time in range(301):
        dt = 1e-5
        theta = t_to_theta(time)
        pos = get_actual_position(theta, config.space)
        _theta = t_to_theta(time - dt)
        _pos = get_actual_position(_theta, config.space)
        ds = list_cartesian_distance(pos, _pos) / 100.0
        print(ds)
        v = ds / dt
        cell = ws.cell(row=2, column=time + 2, value=f"{v[0]:.6f}")
        cell.font = font

        # 更新接下来的点的位置
        current_theta = theta
        _current_theta = _theta
        for i in range(1, 224):
            delta_theta = find_actual_delta_theta(current_theta, config.actual_fixed_distances[0 if i == 1 else 1], config.space)
            current_theta += delta_theta
            pos = get_actual_position(current_theta, config.space)
            _delta_theta = find_actual_delta_theta(_current_theta, config.actual_fixed_distances[0 if i == 1 else 1], config.space)
            _current_theta += _delta_theta
            _pos = get_actual_position(_current_theta, config.space)
            ds = list_cartesian_distance(pos, _pos) / 100.0
            v = ds / dt
            print(time)
            cell = ws.cell(row=i + 2, column=time + 2, value=f"{v[0]:.6f}")
            cell.font = font

    wb.save("result1_v.xlsx")

# dis_xlsx_init()
# dis_fill_xlsx()

# v_xlsx_init()
# v_fill_xlsx()
