#!/usr/bin/python3
'''Define class Square that inherits from Rectangle.'''
from models.rectangle import Rectangle


class Square(Rectangle):
    '''Square inherits from rectangles.'''

    def __init__(self, size, x=0, y=0, id=None):
        '''Initialize instance variables.'''

        super().__init__(size, size, x, y, id)

    def __str__(self):
        '''String representation of class.'''

        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width))

    @property
    def size(self):
        '''get size.'''

        return (self.width)

    @size.setter
    def size(self, value):
        '''Set size.'''

        super().__init__(value, value)

    def update(self, *args, **kwargs):
        '''Updates instance varaibles.'''

        if len(args):
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
