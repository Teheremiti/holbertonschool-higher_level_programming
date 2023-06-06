#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for sub in matrix:
        sep = ""

        for ele in sub:
            print("{}{:d}".format(sep, ele), end="")
            sep = " "

        print()
