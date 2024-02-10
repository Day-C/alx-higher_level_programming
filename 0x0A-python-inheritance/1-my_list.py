#!/usr/bin/python3
'''Define Mylist class.'''


class MyList(list):
    '''Define print_sorted().'''

    def __init__(self, item=[]):
        '''Initialize attributes.'''

        super().__init__(item)

    def print_sorted(self):
        '''Print sorted list.'''

        print(sorted(self))
