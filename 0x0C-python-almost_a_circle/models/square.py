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
