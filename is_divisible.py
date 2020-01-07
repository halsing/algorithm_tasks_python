"""
Number is divisible when it divides by sum of it's numbers
"""


def is_divisible(num):
    num_str = str(num)
    num_sum = 0

    for n in num_str:
        num_sum += int(n)

    return True if num % num_sum == 0 else False
