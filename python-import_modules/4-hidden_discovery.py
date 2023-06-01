#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for File in dir(hidden_4):
        if File[:2] != "__":
            print(File)
