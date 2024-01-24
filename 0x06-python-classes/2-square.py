#!/usr/bin/python3

'''Create class square.'''


class Square:
    '''Structure the class.'''

    def __init__(self, size=0):
        '''Initialize a new square.

        Args:
           size (int): size of square.
        '''
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__Size = size
