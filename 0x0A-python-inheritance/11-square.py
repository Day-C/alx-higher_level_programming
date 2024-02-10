#!/usr/bin/python3
'''Define class Square.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Inherit from Rectangle.'''

    def __init__(self, size):
        '''Initialize attributes.'''

        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        '''Area of square.'''

        return (self.__size * self.__size)

    def __str__(self):
        '''print string prepresentation for class.'''

        return ("[Square] {}/{}".format(self.__size, self.__size))
