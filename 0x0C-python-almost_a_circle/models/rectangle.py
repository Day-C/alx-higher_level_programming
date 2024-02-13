#!/usr/bin/python3
'''Define class Rectangle that inherits from Base.'''
from models.base import Base


class Rectangle(Base):
    '''Inherits from Base class.'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''Initialize instance variables.'''

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super().__init__(id)
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
            raise ValueError("height must be > 0")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        '''Get width.'''
        return self.__width

    @width.setter
    def width(self, value):
        '''Set width.'''

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''Get height.'''
        return self.__height

    @height.setter
    def height(self, value):
        '''Set height.'''

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''Get x.'''
        return self.__x

    @x.setter
    def x(self, value):
        '''Set x.'''

        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        '''Get y.'''
        return self.__y

    @y.setter
    def y(self, value):
        '''Set y.'''

        if isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        '''Method calculats area of rectangle.'''

        return(self.__width * self.__height)

    def display(self):
        '''Method displays 2-d image of rectangle with `#` characters.'''

        if self.__y > 0:
            for i in range(self.__y):
                print()
        for i in range(self.__height):
            if self.__x > 0:
                print(" " * self.__x, end="")
                print("#" * self.__width)
            else:
                print("#" * self.__width)

    def __str__(self):
        '''Method returns str representation of class.'''

        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        '''Method updates instance attributes.'''

        try:
            if args[0]:
                self.id = args[0]
            if args[1]:
                self.__width = args[1]
            if args[2]:
                self.__height = args[2]
            if args[3]:
                self.__x = args[3]
            if args[4]:
                self.__y = args[4]
        except:
            pass

