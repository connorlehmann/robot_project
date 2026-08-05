import math

def cross_product(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

def vector_subtract(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])

def find_t(Q, P, S, R):

    vector_QP = vector_subtract(Q, P)
    numerator = cross_product(vector_QP, S)
    denominator = cross_product(R, S)

    t = numerator / denominator
    return t

def find_u(Q, P, S, R):
    vector_QP = vector_subtract(Q, P)
    numerator = cross_product(vector_QP, R)
    denominator = cross_product(R, S)

    u = numerator / denominator
    return u