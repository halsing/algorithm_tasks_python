"""
Two simple ways to check if number is even
"""


def is_even(number):
    return False if number % 2 or number == 0 else True


even = lambda x: False if x % 2 or x == 0 else True
