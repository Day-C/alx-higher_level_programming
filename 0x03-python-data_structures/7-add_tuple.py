#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    n1, n2, m1, m2 = 0, 0, 0, 0
    tup = []
    if len(tuple_a) == 0:
        n1, n2 = 0, 0
    elif len(tuple_a) == 1:
        n1, n2 = tuple_a[0], 0
    else:
        n1, n2 = tuple_a[:2]
    if len(tuple_b) == 0:
        m1, m2 = 0, 0
    elif len(tuple_b) == 1:
        m1, m2 = tuple_b[0], 0
    else:
        m1, m2 = tuple_b[:2]
    tup.append(n1 + m1)
    tup.append(n2 + m2)
    return (tuple(tup))
