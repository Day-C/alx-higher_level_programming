#!/usr/bin/python3
'''Define Mylist class.'''


class MyList(list):
    '''Define print_sorted().'''

    def print_sorted(self):
        '''Print sorted list.'''

        print(sorted(self))
