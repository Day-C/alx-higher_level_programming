#!/usr/bin/python3

'''Define a class Square.'''


class Square:
    '''Strcture of a square.'''

    def __init__(self, size):
        '''Initialize stucture.'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    @property
    def size(self):
        '''Module retuns size.'''
        return (self.__size)
    @size.setter
    def size(self, value):
        '''Method set new valuew of size.'''
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
    def area(self):
        '''Method returns the suare of a number.'''
        return (self.__size *self.__size)
    def my_print(self):
        '''Method prints a square with '#' characters.'''
        j = 0
        if self.__size != 0:
            for i in range((self.__size * self.__size) - 1):
                if j == self.__size:
                    j = 0
                    print("")
                else:
                    print("#", end="")
                    j += 1
        else:
            print("")
