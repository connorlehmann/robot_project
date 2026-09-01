import math

def cross_product(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]

def vector_subtract(p1, p2):
    return (p1[0] - p2[0], p1[1] - p2[1])

def find_t(Q, P, S, R):
    vector_QP = vector_subtract(Q, P)
    numerator = cross_product(vector_QP, S)
    denominator = cross_product(R, S)
    return numerator / denominator

def find_u(Q, P, S, R):
    vector_QP = vector_subtract(Q, P)
    numerator = cross_product(vector_QP, R)
    denominator = cross_product(R, S)
    return numerator / denominator

def ray_segment_intersect(P, R, Q, S):
    """
    Cast a ray from point P in direction R and test it against the
    segment starting at Q with direction S (i.e. the segment runs
    from Q to Q + S).

    Returns the distance t along the ray to the intersection point,
    or None if there is no valid intersection (ray and segment are
    parallel, the intersection is behind the ray's origin, or the
    intersection point falls outside the actual segment).
    """
    denominator = cross_product(R, S)

    # Ray is parallel to the wall segment (or degenerate) -> no single intersection
    if abs(denominator) < 1e-9:
        return None

    vector_QP = vector_subtract(Q, P)
    t = cross_product(vector_QP, S) / denominator
    u = cross_product(vector_QP, R) / denominator

    # t < 0  -> intersection is behind the ray's origin (wrong direction)
    # u not in [0, 1] -> intersection is on the wall's infinite line,
    #                     but off the actual wall segment
    if t >= 0 and 0 <= u <= 1:
        return t

    return None
