#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):

    matrix = [[234], [567], [891]]

    x = '\n'.join([''.join(['{:3}'.format(item) for item in row]) for now in matrix])

    print(x)
