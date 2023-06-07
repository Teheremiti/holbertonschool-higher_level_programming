#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    value = 0
    best = None
    for k, v in a_dictionary.items():
        if v > value:
            best = k
            value = v

    return best
