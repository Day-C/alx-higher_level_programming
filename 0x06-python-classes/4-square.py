#!/usr/bin/#!/usr/bin/python3
'''Create a class Square.'''


class Square:
    '''Structure class.'''
    

    def __init__(self, size=0):
        '''Initialize variables.'''

        if not isinstance(size, int):
            raise TypeError("size most be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._size = size

    def area(self):
        '''Method returns the square area.'''
        return (self._size * self._size)
    def size(self):
        return size = size)
