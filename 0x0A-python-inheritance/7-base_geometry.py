#!/usr/bin/python3
'''Define class BaseGeometry.'''


class BaseGeometry:
    '''Class basegeometry.'''

    def area(self):
        '''Method returns exception.'''

        raise Exception("area{} is not implemented")

    def integer_validator(self, name, value):
        '''Method validates value.'''

        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> n=must be greater than 0")
