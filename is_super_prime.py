def is_prime(n):
    for i in range(n):
        if i <= 1 or n % i != 0:
            pass
        elif n % i == 0:
            return False

def is_super_prime(n):
    str_num = str(n)
    prime = False if is_prime(n) is False else True

    if prime:
        sum = 0
        for s in str_num:
            sum += int(s)
        prime = False if is_prime(sum) is False else True

    return prime