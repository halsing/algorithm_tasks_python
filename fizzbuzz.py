"""
Just a fizzbuzz
Fizzbuzz is a program which generate numbers from 1 to n and check:
If current number is divisible by 3 then print 'Fizz'
If current number is divisible by 5 then print 'Buzz'
But if current number is divisible by 3 and 5 than print 'FizzBuzz
"""


def fizz_buzz(n: int) -> None:

    for x in range(1,n+1):
        if x % 15 == 0:
            print(x, "FizzBuzz")
        elif x % 5 == 0:
            print(x, "Buzz")
        elif x % 3 == 0:
            print(x, "Fizz")


def fizz_buzz_one_line(n: int) -> None:
    for x in range(1,n+1):
        print(x, "FizzBuzz") if x % 15 == 0 else print(x, "Buzz") if x % 5 == 0 else print(x, "Fizz") if x % 3 == 0 else None


