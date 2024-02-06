#!/usr/bin/python3
'''Define function read_file().'''

def read_file(filename=""):
    '''Read contents of file.'''

    with open(filename) as f:
        print(f.read(), end = "")
