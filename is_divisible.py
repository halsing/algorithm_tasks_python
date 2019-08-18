#liczba podzielna = liczba dzieli się przez sumę swoich liczb
def is_divisible(num):
    num_str = str(num)
    num_sum = 0

    for n in num_str:
        num_sum += int(n)

    print("is divisible") if num % num_sum == 0 else print("isn't divisible")