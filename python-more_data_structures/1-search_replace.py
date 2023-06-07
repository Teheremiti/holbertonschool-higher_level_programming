#!/usr/bin/python3
def search_replace(my_list, search, replace):
    replaced = []
    for ele in my_list:
        if ele == search:
            replaced.append(replace)
        else:
            replaced.append(ele)

    return replaced
