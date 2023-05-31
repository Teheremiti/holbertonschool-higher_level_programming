#!/usr/bin/python3

for tens in range(9):
    for units in range(tens + 1, 10):
        if (tens != units):
            print(f"{tens}{units}", end="")
        if (tens != 8):
            print(", ", end="")

print()
