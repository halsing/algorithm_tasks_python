def is_even(number):
    answer = "isn't even" if number % 2 or number == 0 else "is even"
    return answer


even = lambda x: False if x % 2 or x == 0 else True


even_str = lambda x: "isn't even" if x % 2 or x == 0 else "is even"
