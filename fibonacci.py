def fibonacci(n):
    list = []
    for x in range(n+1):
        if x <= 1:
            list.append(x)
        else:
            list.append(list[-2]+list[-1])

    return list


def fibonacci_check(n):
    if n < 10:
        list = fibonacci(n+1)
    elif n < 45:
        list = fibonacci(int(n/2))
    else:
        list = fibonacci(int(n/4))

    if n in list:
        return f"Liczba {n} jest w ciągu fibonacciego"
    else:
        return f"Liczby {n} nie jest w ciągu fibonacciego"