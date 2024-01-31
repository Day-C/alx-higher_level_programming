#!/usr/bin/python3
'''Define functio 'matrix_divided'.'''


def matrix_divided(matrix, div):
    '''
    function divides elementby div arg
    '''
    new_matrix = []
    index = 0

    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not type(div)  == int:
        if not type(div) == float:
            raise TypeError("div must be a number")

    for n in range(len(matrix)):
        if isinstance(matrix[n], list):
            if n != 0:
                if len(matrix[n-1]) != len(matrix[n]):
                    raise TypeError("Each row of matrix must have the same size")

            for i in matrix[n]:
                if isinstance(i, int) or isinstance(i, float):
                    continue
                else:
                    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        else:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")


    for row in matrix:
        a = []
        for element in row:
            a.append(round(int(element) / div, 2))
        new_matrix.append(a)
    return (new_matrix)
