#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    b = number % 10
    print("{}" .format(b), end='')
    return (b)
