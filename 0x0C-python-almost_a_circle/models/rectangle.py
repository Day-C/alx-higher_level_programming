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
        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if type(self.__height) is not int:
            raise TypeError("height must be an integer")
        if type(self.__x) is not int:
            raise TypeError("x must be an integer")
        if type(self.__y) is not int:
            raise TypeError("y must be an integer")
        if self.__width <= 0:
            raise ValueError("width must be > 0")
        if self.__height <= 0:
            raise ValueError("height must be > 0")
        if self.__x < 0:
            raise ValueError("x must be >= 0")
        if self.__y < 0:
            raise ValueError("y must be >= 0")

    @property
    def width(self):
        '''Get width.'''

        return self.__width

    @width.setter
    def width(self, value):
        '''Set width.'''

        if type(value) is not int:
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

        if type(value) is not int:
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

        if type(value) is not  int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        '''Get y.'''

        return self.__y

    @y.setter
    def y(self, value):
        '''Set y.'''

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
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

        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.__width = arg
                elif i == 2:
                    self.__height = arg
                elif i == 3:
                    self.__x = arg
                elif i == 4:
                    self.__y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.__width = kwargs["width"]
            if "height" in kwargs:
                self.__height = kwargs["height"]
            if "x" in kwargs:
                self.__x = kwargs["x"]
            if "y" in kwargs:
                self.__y = kwargs['y']

    def to_dictionary(self):
        '''Show dictionary representation of instance.'''

        new_dict = {}
        if self.__width:
            new_dict["width"] = self.__width
        if self.__height:
            new_dict["height"] = self.__height
        if self.__x:
            new_dict["x"] = self.__x
        if self.__y:
            new_dict["y"] = self.__y
        if self.id:
            new_dict["id"] = self.id
        return new_dict
