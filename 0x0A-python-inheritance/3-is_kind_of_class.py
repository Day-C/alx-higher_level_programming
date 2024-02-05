#!/usr/bin/python3
'''Define function is_kind_of_class.'''

def is_kind_of_class(obj, a_class):
    '''Check if object is an instance of class.'''
    if isinstance(obj, a_class):
        return (True)
    else:
        return (False)
