#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    for num in my_list:
        if my_list.count(num) == 1:
            res += num

    return res
