#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    doubled = {}
    for key in a_dictionary:
        doubled[key] = a_dictionary[key] * 2

    return doubled
