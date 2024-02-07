#!/usr/bin/python3
'''Define a function class_to_json().'''


def class_to_json(obj):
    '''Convert class to json string.'''

    return ((obj.__dict__))
