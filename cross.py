import numpy as np
from mpmath.math2 import sqrt2

# 2 dot -> 4 edge
lambda_of_head = 27.5 / 286
lambda_of_not_head = 27.5 / 165
lambda_move_head = 15 / 286
lambda_move_not_head = 15 / 165
def cal_long_side(front_dot, back_dot, head):
    back_front_vector = front_dot - back_dot
    if head:
        front_end = np.array([(lambda_of_head + 1) * front_dot[0] - lambda_of_head * back_dot[0],
                              (lambda_of_head + 1) * front_dot[1] - lambda_of_head * back_dot[1]])
        back_end  = np.array([(lambda_of_head + 1) * back_dot[0] - lambda_of_head * front_dot[0],
                              (lambda_of_head + 1) * back_dot[1] - lambda_of_head * front_dot[1]])
        move_vector = np.array([back_front_vector[1] * lambda_move_head, - back_front_vector[0] * lambda_move_head])
    else :
        front_end = np.array([(lambda_of_not_head + 1) * front_dot[0] - lambda_of_not_head * back_dot[0],
                              (lambda_of_not_head + 1) * front_dot[1] - lambda_of_not_head * back_dot[1]])
        back_end  = np.array([(lambda_of_not_head + 1) * back_dot[0] - lambda_of_not_head * front_dot[0],
                              (lambda_of_not_head + 1) * back_dot[1] - lambda_of_not_head * front_dot[1]])
        move_vector = np.array([back_front_vector[1] * lambda_move_not_head, - back_front_vector[0] * lambda_move_not_head])
    # print(front_end + move_vector, back_end + move_vector, front_end - move_vector, back_end - move_vector)
    return front_end + move_vector, back_end + move_vector, front_end - move_vector, back_end - move_vector

cal_long_side(np.array([0,0]), np.array([165 * sqrt2 / 2, 165 * sqrt2 / 2]), False)


# return true if 2 edges cross
def cross_test(A0, A1, B0, B1):
    A0B0 = B0 - A0
    A0B1 = B1 - A0
    A0A1 = A1 - A0

    vector1 = np.cross(A0A1, A0B0)
    vector2 = np.cross(A0A1, A0B1)

    B0A0 = -A0B0
    B0A1 = A1 - B0
    B0B1 = B1 - B0

    vector3 = np.cross(B0B1, B0A0)
    vector4 = np.cross(B0B1, B0A1)

    # print(vector1, vector2)
    # print(vector3, vector4)
    return vector1 * vector2 <= 0 and vector3 * vector4 <= 0


