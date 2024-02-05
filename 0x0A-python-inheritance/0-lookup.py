#!/usr/bin/python3
'''Define a fucntion loopup().'''

def lookup(obj):
    '''Returns info about an object.'''

    return list((obj.__dict__))
