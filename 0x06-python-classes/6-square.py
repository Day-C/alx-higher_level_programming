#!/usr/bin/python3

'''Define a class Square.'''


class Square:
    '''Strcture of a square.'''

    def __init__(self, size=0, position=(0, 0)):
        '''Initialize stucture.'''

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif not isinstance(position, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
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
        return (self.__size * self.__size)

    def my_print(self):
        '''Method prints a square with '#' characters.'''
        j = 0
        if self.__size != 0:
            if not isinstance(self.__position[1], int):
                raise TypeError("position must be a tuple of 2 positive integers")
            if self.__position[1] > 0:
                print("")
                for i in range(self.__size):
                    print("{}".format(" " * self.__position[0]), end="")
                    for j in range(self.__size):
                        print("#", end="")
                    print("")
            else:
                for i in range(self.__size):
                    print("{}".format(" " * self.__position[0]), end="")
                    for j in range(self.__size):
                        print("#", end="")
                    print("")
        else:
            print("")

    @property
    def position(self):
        '''Method gets position.'''
        return (self.__position)

    @position.setter
    def position(self, value):
        '''Method setts position.'''
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
