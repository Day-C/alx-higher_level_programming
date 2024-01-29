#!/usr/bin/python3

'''Define class Ractangle.'''


class Rectangle:
    '''Class instance.'''

    def __init__(self, width=0, height=0):
        '''Initialize attribules.

        Args:
            width (int): value for attribute witdth
            height (int): valuse for attriute height
        '''

        if not isinstance(width, int):
            if not isinstance(width, float):
                raise TypeError("width must be an integer")
            width = int(width)
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            if not isinstance(heigh, float):
                raise TypeError("height must be an integer")
            height = int(height)
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Retirive width.'''

        return (self.__width)

    @width.setter
    def width(self, value):
        '''Setter width.'''

        if not isinstance(value, int):
            if not isinstance(value, float):
                raise TypeError("width must be an integer")
            value = int(value)
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        '''Retrive height.'''

        return (self.__height)

    @height.setter
    def height(self, value):
        '''Setter height.'''

        if not isinstance(value, int):
            if not isinstance(value, float):
                raise TypeError("height must be an integer")
            value = int(value)
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        '''Area of rectangle'''

        if self.__height == 0 or self.__width == 0:
            return (0)
        return(self.__height * self.__width)

    def perimeter(self):
        '''Perimeter of rectangle.'''

        if self.__height == 0 or self.__width == 0:
            return (0)
        return ((self.__height * 2) + (self.__width * 2))

    def __str__(self):
        '''String representation of instance'''

        string = []
        i = 0
        j = 1
        while i < (self.__height * self.__width):
            print("#", end = "")
            if j == self.__width and i < (self.__height *self.__width):
                j = 0
                print()
            i += 1
            j += 1
        return ('')
