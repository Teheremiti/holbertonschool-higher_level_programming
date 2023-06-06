#!/usr/bin/python3
def no_c(my_string):
    new = ""
    for element in my_string:
        if element != "c" and element != "C":
            new += element

    return new
