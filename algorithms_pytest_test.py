import pytest

from fibonacci import fibonacci, fibonacci_check
from is_divisible import is_divisible
from is_even import is_even
from is_prime import is_prime, is_prime_recurent, is_prime_line
from is_super_prime import is_super_prime, is_super_prime_small, f
from palindrom import is_palindrom
from pascal_triangle import pascal_triangle
from problem_wydawania_reszty import reszta


# ------------------------------ fibonacci ----------------------------------
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


# ------------------------------ is_divisible ----------------------------------
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


# ------------------------------ is_even ----------------------------------
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


# ------------------------------ is_prime ----------------------------------
IS_PRIME = (
        (2, True),
        (12, False),
        (5, True),
        (7, True),
        (22, False),
        (0, True),
        (11, True),
        (13, True),
)


@pytest.mark.parametrize('number, expected', IS_PRIME)
def test_is_prime(number, expected):
    assert is_prime(number) == expected


@pytest.mark.parametrize('number, expected', IS_PRIME)
def test_is_prime_recurent(number, expected):
    assert is_prime_recurent(n=number) == expected


@pytest.mark.parametrize('number, expected', IS_PRIME)
def test_is_prime_line(number, expected):
    assert is_prime_line(number) == expected


# ------------------------------ is_super_prime --------------------------------
IS_SUPER_PRIME = (
        (7, True),
        (23, True),
        (29, True),
        (41, True),
        (43, True),
        (2, True),
        (4, False),
        (10, False),
        (31, False),
        (17, False),
        (19, False),
)


@pytest.mark.parametrize('number, expected', IS_SUPER_PRIME)
def test_is_super_prime(number, expected):
    assert is_super_prime(number) == expected


@pytest.mark.parametrize('number, expected', IS_SUPER_PRIME)
def test_is_super_prime_small(number, expected):
    assert is_super_prime_small(number) == expected


@pytest.mark.parametrize('number, expected', IS_SUPER_PRIME)
def test_is_prime_lambda_f(number, expected):
    assert f(number) == expected
