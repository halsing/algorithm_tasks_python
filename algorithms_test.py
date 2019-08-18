import pytest

from fibonacci import fibonacci, fibonacci_check
from is_divisible import is_divisible
from is_even import is_even
from is_prime import is_prime
from is_super_prime import is_super_prime
from palindrom import is_palindrom
from pascal_triangle import pascal_triangle
from problem_wydawania_reszty import reszta

#------------------------------ fibonacci ----------------------------------
@pytest.mark.parametrize('number, expected_list', (
        (1, [0]),
        (2, [0, 1]),
        (3, [0, 1, 1]),
        (4, [0, 1, 1, 2]),
        (5, [0, 1, 1, 2, 3]),
        (6, [0, 1, 1, 2, 3, 5, ]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]),
))
def test_fibonaci(number, expected_list):
    assert fibonacci(number) == expected_list


@pytest.mark.parametrize('number, expected', (
        (1, True),
        (5, True),
        (12, False),
        (18, False),
        (21, True),
        (0, True),
))
def test_fibonacci_check(number, expected):
    assert fibonacci_check(number) is expected

#------------------------------ is_divisible ----------------------------------
@pytest.mark.parametrize('number, expected', (
        (2, True),
        (12, True),
        (18, True),
        (111, True),
        (21, True),
        (16, False),
        (17, False),
        (55, False),
))
def test_is_divisible(number, expected):
    assert is_divisible(number) is expected


#------------------------------ is_even ----------------------------------
@pytest.mark.parametrize('number, expected', (
        (2, "is even"),
        (12, "is even"),
        (18, "is even"),
        (1122, "is even"),
        (22, "is even"),
        (0, "isn't even"),
        (1, "isn't even"),
        (111, "isn't even"),
))
def test_is_even(number, expected):
    assert is_even(number) == expected
