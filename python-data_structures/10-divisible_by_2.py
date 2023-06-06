#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    even = []
    for ele in my_list:
        if ele % 2 == 0:
            even.append(True)

        else:
            even.append(False)

    return even
