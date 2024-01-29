#!/usr/bin/python3
Rectangle = __import__('1-rectangle').Rectangle

my_rectangle = Rectangle()
print(my_rectangle.__dict__)

my_rectangle.width = 5
my_rectangle.height = 12.125
print(my_rectangle.__dict__)
