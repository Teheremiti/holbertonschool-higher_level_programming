#!/bin/usr/python3
def uppercase(str):
    for letter in str:
        _ascii = ord(letter)
        if _ascii >= 97 and _ascii <= 122:
            _ascii -= 32
        print("{}".format(chr(_ascii)), end="")
    print()
