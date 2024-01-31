#!/usr/bin/python3
'''Define class.'''


class LockedClass:
    '''Define variavles.'''

    __slots__ = ["first_name"]
    def set_name(self, name):
        self.__slots__[0] = name

    def get_first_name(self):
        self.__slots__[0]
