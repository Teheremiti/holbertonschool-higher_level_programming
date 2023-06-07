#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = {ele for ele in my_list}
    result = 0
    for num in my_set:
        result += num

    return result
