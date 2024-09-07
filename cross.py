import numpy as np
from astropy.modeling.functional_models import Box1D
from mpmath.math2 import sqrt2
from statsmodels.tsa.statespace.simulation_smoother import check_random_state

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

# cal_long_side(np.array([0,0]), np.array([165 * sqrt2 / 2, 165 * sqrt2 / 2]), False)


# return true if 2 edges cross
def cross_test(edge1, edge2):
    A0 = edge1[0]
    A1 = edge1[1]
    B0 = edge2[0]
    B1 = edge2[1]

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

    #print(vector1, vector2)
    #print(vector3, vector4)
    return vector1 * vector2 <= 0 and vector3 * vector4 <= 0

#print(cross_test(np.array([[0,0],[1,0]]),np.array([[0,-1],[0.000,0.3]])))

def all_cross_check(dot_matrix):
    edge_list = []
    for i in range(dot_matrix.shape[0] - 1):
        A0, A1, B0, B1 = cal_long_side(dot_matrix[i], dot_matrix[i + 1], i == 0)
        edge_list.append(np.array([A0, A1])) # even：inside
        edge_list.append(np.array([B0, B1])) # odd: outside

    cross = False
    for i in range(2, len(edge_list), 2):
        for j in range(i - 3, 0, -2):
            print(i, j)
            if cross_test(edge_list[i], edge_list[j]):
                cross = True
                break
        if cross:
            break

    return cross

#print(all_cross_check(np.array([[0,0],[386,0],[386 + 165, 0]])))
