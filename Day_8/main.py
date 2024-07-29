# Function parameters

import math


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def greet(name):
    print(f"Hello {name}. Welcome to 100 Days of code challenge.")


greet("Dileep")

# Positional and keyword arguments


def greet(name, location):
    print(f"Hello {name}. Welcome to 100 Days of code challenge.")
    print(f"How's the wether in {location}?")


greet("Texas", "Dileep")  # Positional argument
greet(location="Texas", name="Dileep")  # Keyword argument


def sum_of_nums(a, b):
    return a+b


"""
You are painting a wall. The instructions on the paint can says that 1 can of paint can cover 5 square meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height x wall width) ÷ coverage per can.
"""


def paint_calc(height, width, cover):
    print(f"You'll need {math.ceil(height*width/cover)} cans of paint.")


test_h = int(input())  # Height of wall (m)
test_w = int(input())  # Width of wall (m)
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)

# Prime number checker


def prime_checker(number):
    for i in range(2, number):
        if number % i == 0:
            print("It's not a prime number.")
            break
    else:
        print("It's a prime number.")


n = int(input())  # Check this number
prime_checker(number=n)