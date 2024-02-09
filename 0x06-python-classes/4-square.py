#!/usr/bin/python3

'''Create a class Square.'''


class Square:
    '''Structure class.'''

    def __init__(self, size=0):
        '''Initialize variables.
        Arg: size'''
        if not isinstance(size, int):
            raise TypeError("size most be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    
    @property
    def size(self):
        '''Method gets the current size of square.'''
        return (self.__size)
    
    @size.setter
    def size(self, value):
        '''Method sets the value of a square.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        '''Method returs the area of that square.'''
        return (self.__size * self.__size)
