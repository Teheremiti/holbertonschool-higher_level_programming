#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string is None:
        return 0

    numerals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
    }

    result = 0
    previous = 0
    for char in roman_string:
        if previous < numerals[char]:
            result += numerals[char] - previous * 2

        else:
            result += numerals[char]

        previous = numerals[char]

    return result
