#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    Sum = 0
    for i in range(1, len(argv)):
        Sum += int(argv[i])

    print(Sum)
