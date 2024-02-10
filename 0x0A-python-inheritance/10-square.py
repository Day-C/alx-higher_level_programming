#!/usr/bin/python3
'''Define class Square.'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Inherit from Rectangle.'''

    def __init__(self, size):
        '''Initialize attributes.'''

        super().__init__(size, size)
