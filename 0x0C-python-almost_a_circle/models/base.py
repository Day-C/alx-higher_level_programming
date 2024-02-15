#!/usr/bin/python3
'''Define class Base.'''
import json


class Base:
    '''Base of all other classes.'''
    __nb_objects = 0

    def __init__(self, id=None):
        '''Initialize instance vars
        Args:
            id(int)
        '''

        if id is None:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
        elif id is not None:
            self.id = id

    def to_json_string(list_dictionaries):
        '''Represent contents of list_dictionaries in json string.'''

        return json.dumps(list_dictionaries)
