#!/usr/bin/python3
'''Define function append_write():'''


def append_write(filename="", text=""):
    '''Append text to end of file.'''

    with open(filename, 'a') as f:
        return (f.write(text))
