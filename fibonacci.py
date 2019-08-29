def fibonacci(n):
    lists = []
    for x in range(n):
        if x <= 1:
            lists.append(x)
        else:
            lists.append(lists[-2]+lists[-1])

    return lists


def fibonacci_check(n):
    if n < 10:
        lists = fibonacci(n+3)
    elif n < 45:
        lists = fibonacci(int(n/2))
    else:
        lists = fibonacci(int(n/4))

    return True if n in lists else False
