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
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")

        self.__width = width
        self.__height = height

    @property
    def width(self):
        '''Retirive width.'''

        return (self.width)
    @width.setter
    def width(self, value):
        '''Setter width.'''

        if value < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(value, int):
            raise TypeError("width mist be an integer")
        self.__width = value

    @property
    def height(self):
        '''Retrive height.'''

        return (self.height)

    @height.setter
    def height(self, value):
        '''Setter height.'''

        if value < 0:
            raise ValueError("height must be >= 0")
        if not isinstance(value, int):
            raise TypeError("height mus be a integer")
        self.__height = value
