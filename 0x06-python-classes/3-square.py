#!/usr/bin/python3

'''Create a class Square.'''


class Square:
    '''Structure class.'''
    def __init__(self, size=0):
        '''Initialize variables.
        size'''
        if not isinstance(size, int):
            raise TypeError("size most be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        '''Method returns the square area.'''
        return (self.__size * self.__size)
