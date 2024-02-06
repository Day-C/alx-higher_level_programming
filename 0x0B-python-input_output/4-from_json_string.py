#!/usr/bin/python3
'''Define function from _json_string().'''
import json


def from_json_string(my_str):
    '''Convert json string to original object.'''

    return (json.loads(my_str))
