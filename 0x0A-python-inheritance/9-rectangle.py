#!/usr/bin/python3
''' Define a class Rectangle.'''
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Class inherits from BaseGeometry.'''

    def __init__(self, width, height):
        '''Initialize instance variables.'''

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__height = height
        self.__width = width


    def area(self):
        return (self.__width * self.__height)

    def print(self):
        print("[Rectangle] {}/{}".format(self.__width, self.__height))

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
