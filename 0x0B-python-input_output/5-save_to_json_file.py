#!/usr/bin/python3
'''Define function save_to_json_file().'''
import json


def save_to_json_file(my_obj, filename):
    '''Convert object to json_string ans save in file.'''

    with open(filename, 'w', encoding="utf-8") as f:
        f.write = json.dumps(my_obj)
        print(json.dumps(my_obj))
        return (my_obj)
