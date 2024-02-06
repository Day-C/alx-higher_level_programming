#!/usr/bin/python3
'''Define function read_file().'''

def read_file(filename="", encoding = "utf-8"):
    '''Read contents of file.'''

    with open(filename) as f:
        print(f.read(), end = "")
