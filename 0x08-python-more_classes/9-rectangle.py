#!/usr/bin/python3

'''Define class Ractangle.'''


class Rectangle:
    '''Class instance.'''

    print_symbol = "#"
    number_of_instances = 0
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

        type(self).number_of_instances += 1
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
            print(self.print_symbol, end = "")
            if j == self.__width:
                if i == (self.__height *self.__width) - 1:
                    break
                j = 0
                print()
            i += 1
            j += 1
        return ('')

    def __repr__(self):
        '''Return string representation of object.'''

        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        '''Static class.'''

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if Rectangle.area(rect_1) == Rectangle.area(rect_2):
            return (rect_1)
        if  Rectangle.area(rect_1) > Rectangle.area(rect_2):
            return (rect_1)
        else:
            return (rect_2)

    @classmethod
    def square(cls, size=0):
        '''Class method.'''

        self.__width = size
        self.__height = size
        cls.__str__
        return cls
