#!/usr/bin/python3
sep = ""

for tens in range(9):
    for units in range(tens + 1, 10):
        if (tens != units):
            print(f"{sep}{tens}{units}", end="")

        sep = ", "

print()
