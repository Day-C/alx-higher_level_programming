#!/usr/bin/python3
def add_integer(a, b=98):
    '''
        The function adds integer arguments.
    '''
    if not type(a) == int:
        if not type(a) == float:
            raise TypeError("a must be an integer")
        a = int(a)
    elif not type(b) == int:
        if not type(b) == float:
            raise TypeError("b must be an integer")
        b = int(b)
    return (a + b)
