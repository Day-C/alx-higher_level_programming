#!/usr/bin/python3
''' Define a class Rectangle.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class inherits from BaseGeometry.'''

    def __init__(self, width, height):
        '''Initialize instance variables.'''

        if super().integer_validator("width", width):
            self.__width = width
        if super().integer_validator("height", height):
            self.__height - height
