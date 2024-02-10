#!/usr/bin/python3
'''Define class node.'''


class Node():
    '''class defines node of liked list'''

    def __init__(self, data, next_nod=None):
        '''Initialize instance variables.'''
        if not isinstance(data, int):
            raise TypeError("data must be aninteger")
        if next_node is not None:
            if isinstance(type(next_node), object):
                raise TypeError("next_node must be a Node object")
        self.__data = data
        self.__next_node = nest_node

    @property
    def data(self):
        '''Methodgets data.'''
        return self.__data

    @data.setter
    def data(self, value):
        '''Method setts data.'''
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = Value

    @property
    def next_node(self):
        '''Method gets new_node.'''
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        '''Method setts next_node.'''
        if value is not None:
            if not isinstance(type(value), object):
                raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList(Node):
    '''Define a new class singlylinkedlist.'''

    def __init__(self):
        '''Initialize variables.'''
        self.__head = []

    def sorted_insert(self, value):
        '''Insert item in sortedorder'''
        self.__head.append(value)

    def __str__(self):
        '''Method prints content of class.'''
        if len(self.__head) > 1:
            lis = sorted(self.__head)
            for i in range(len(lis)):
                if i < len(lis)-1:
                    print("{}".format(lis[i]))
            return str(format(lis[i]))
        else:
            return("")
