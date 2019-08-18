# Napisz program, który wyświetla liczby od 1 do 100.
# Dla liczb podzielnych przez 3 niech program wyświetli „Fizz”;
# dla liczb podzielnych przez 5 niech wyświetli ‚Buzz’;
# a dla liczb podzielnych przez 15 niech wyświetli ‚FizzBuzz’.

def fizz_buzz(n):

    for x in range(1,n+1):
        if x % 15 == 0:
            print(x,"FizzBuzz")
        elif x % 5 == 0:
            print(x,"Buzz")
        elif x % 3 == 0:
            print(x,"Fizz")