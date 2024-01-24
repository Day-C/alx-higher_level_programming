#!/usr/bin/python3
'''Create class square.'''

class Square:
    '''Structure the class.'''

    def __init__(self, size=0):
        '''Try clause cheks if size is an integer.'''
        try:
            size += 0
        except:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Size = size
        
