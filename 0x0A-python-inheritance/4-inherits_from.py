#!/usr/bin/python3
'''Define function inherits_from.'''


def inherits_from(obj, a_class):
    '''Check if object is an instance of inherited class.'''

    if type(obj) is not a_class and issubclass(type(obj), a_class):
        return (True)
    else:
        return (False)
