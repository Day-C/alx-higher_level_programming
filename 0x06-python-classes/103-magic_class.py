#!/usr/bin/python3

'''Define a class MAgicClass.'''
import math


class MagicClass:
    '''structure a circle'''

    def __init__(self, radius=0):
        '''Intiialize the circle
       
        Args:
            rarious: (loat or int) radious of the circle
        '''
        self.__redius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radious must be a number")
        self.__radius = radius

        def area(self):
            '''Method returns the area of a circle.'''
            return (self.__radius ** 2 * math.pi)
        def curcymference(self):
            '''Method returns the circumference of a circle.'''
            return (2 * math.pi * self.radius)
