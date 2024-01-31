#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [2, 4, 5, 6]
]
#print(matrix_divided(matrix, 3))
print(matrix)
try:
    matrix_divided(matrix, "White")
except Exception as e:
    print(e)
