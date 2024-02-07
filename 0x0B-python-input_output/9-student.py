#!/usr/bin/python3
'''Define class Student.'''


class Student:
    '''Define attributes of student.'''

    def __init__(self, first_name, last_name, age):
        '''Initialize public attributes.'''

        self.first_name = first_name;
        self.last_name = last_name;
        self.age = age;

    def to_json(self):
        '''Retrive dictionary representation of a Student instance.'''

        return (self.__dict__)
