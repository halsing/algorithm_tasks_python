def is_prime(n):
    num = n
    prime = True
    for i in range(n):
        if i <= 1 or num % i != 0:
            pass
        elif num % i == 0:
            prime = False

    print("is Prime") if prime else print("isn't Prime")
