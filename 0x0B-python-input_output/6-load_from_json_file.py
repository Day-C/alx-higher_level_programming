#!/usr/bin/python3
'''Define function load_from_json().'''
import json


def load_from_json_file(filename):
    '''Function creates objects from content of json file.'''

    with open(filename, encoding="utf-8") as f:
            data = f.read()
            return (json.loads(data))
