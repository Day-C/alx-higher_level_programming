#!/usr/bin/python3
'''Define function write_file().'''


def write_file(filename="", text=""):
    '''Write text into file.'''

    with open(filename, 'w') as f:
        return (f.write(text))
