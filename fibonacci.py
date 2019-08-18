def fibonacci(n):
    list = []
    for x in range(n):
        if x <= 1:
            list.append(x)
        else:
            list.append(list[-2]+list[-1])

    return list


def fibonacci_check(n):
    if n < 10:
        list = fibonacci(n+3)
    elif n < 45:
        list = fibonacci(int(n/2))
    else:
        list = fibonacci(int(n/4))

    return True if n in list else False