"""
Fibonacci module can return list of fibonacci number
or check if number is in fibonacci list
"""

def fibonacci(n):
    """
    Return list of fibonacci numbers
    """
    lists = []
    for x in range(n):
        if x <= 1:
            lists.append(x)
        else:
            lists.append(lists[-2]+lists[-1])

    return lists


def fibonacci_check(n):
    """
    Check if n is in fibonacci list
    """
    if n < 10:
        lists = fibonacci(n+3)
    elif n < 45:
        lists = fibonacci(int(n/2))
    else:
        lists = fibonacci(int(n/4))

    return True if n in lists else False
