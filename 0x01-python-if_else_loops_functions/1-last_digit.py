#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    b = abs(number)
if number >= 0:
    a = number % 10
else:
    a = (b % 10) * (-1)
if a > 5:
    print(f"last digit of {number:d} is {a:d} and is greater than 5")
elif a == 0:
    print(f"Last digit of {number:d} is {a:d} and  is 0")
elif a < 6 and a != 0:
    print(f"last digit of {number:d} is {a:d} and is less than 6 and not 0")
