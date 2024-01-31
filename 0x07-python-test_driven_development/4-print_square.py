#!/usr/bin/python3
'''Define function to print '#' characters.'''

def print_square(size):
    '''
    function prints '#' characters to form  a square
    '''
    j = 0
    if not isinstance(size, int):
        if not isinstance(size, float):
            raise TypeError("size must be an integer")
    if type(size) == float:
        size = int(size)
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(0, int(size)):
        while j < int(size):
            j += 1
            print("#", end="")
        print()
        j = 0

