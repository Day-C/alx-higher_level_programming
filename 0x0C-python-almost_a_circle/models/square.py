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

        return ("[Square] ({}) {}/{} - {}".format(self.width, self.x, self.y, self.width))
