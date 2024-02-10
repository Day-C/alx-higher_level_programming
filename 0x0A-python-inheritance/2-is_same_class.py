#!/usr/bin/python3
'''Define class is_same_class.'''


def is_same_class(obj, a_class):
    '''Checks if object is an instance of specified class.'''

    if type(obj) == a_class:
        return (True)
    else:
        return (False)
