"""
Module contain a few different functions to check if number is prime
"""

def is_prime(n):
    num = n
    prime = True
    for i in range(n):
        if i <= 1 or num % i != 0:
            pass
        elif num % i == 0:
            prime = False
            break

    return prime


def is_prime_recurent(n, current=2):
    if n <= 1 or n == current:
        return True
    elif n % current:
        return is_prime_recurent(n, current + 1)
    else:
        return False


def is_prime_line(n, c=2):
    return True if n <= 1 or n == c else is_prime_line(n ,c+1) if n % c else False
