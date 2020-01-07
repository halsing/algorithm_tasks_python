"""
Number is super prime when is prime and sum of it's number is prime
"""
from is_prime import is_prime_recurent as ipr


def is_super_prime(n):
    str_num = str(n)
    prime = ipr(n)

    if prime:
        sums = 0
        for s in str_num:
            sums += int(s)
        prime = ipr(sums)

    return prime


def is_super_prime_small(n):
    return True if ipr(n) and ipr(sum([int(s) for s in str(n)])) else False


f = lambda n: True if ipr(n) and ipr(sum([int(s) for s in str(n)])) else False
