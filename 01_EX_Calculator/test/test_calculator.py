from app.calculator import *

import pytest
import approxe from pytest
# use pytest approxe if you deal with floats
#
# Positive testing
#
def test_add_4_to_13_is_17():
    # Arrange
    number_1 = 4
    number_2 = 13
    expected = 17

    # Act
    result = sum_numbers(number_1, number_2)

    # Assert
    assert result == expected

def test_add_15_to_21_is_36():
    # Arrange, Act and Assert in one line
    assert sum_numbers(15, 21) == 36

def test_add_minus_4_to_5_is_1():
    assert sum_numbers(-4, 5) == 1

#
# subtract_numbers tests
#
def test_subtract_10_minus_3_is_7():
    assert subtract_numbers(10, 3) == 7

def test_subtract_5_minus_10_is_minus_5():
    assert subtract_numbers(5, 10) == -5, "this test sould return -5"

def test_subtract_0_minus_0_is_0():
    assert subtract_numbers(0, 0) == 0

#
# multiply_numbers tests
#
def test_multiply_3_times_4_is_12():
    assert multiply_numbers(3, 4) == 12

def test_multiply_minus_2_times_5_is_minus_10():
    assert multiply_numbers(-2, 5) == -10

def test_multiply_0_times_100_is_0():
    assert multiply_numbers(0, 100) == 0

#
# divide_numbers tests
#
def test_divide_10_by_2_is_5():
    assert divide_numbers(10, 2) == 5

def test_divide_9_by_3_is_3():
    assert divide_numbers(9, 3) == 3

def test_divide_5_by_2_is_2_point_5():
    assert divide_numbers(5, 2) == 2.5

def test_divided_by_0_raises_exception():
    with pytest.raises(ValueError):
        divide_numbers(10, 0)

#
# Negative testing
#
def test_add_1_to_1_is_not_1():
    assert not sum_numbers(1, 1) == 1

#
# Data type testing
#
def test_add_two_numbers_returns_a_number():
    assert isinstance(sum_numbers(4, 5), (int, float))

def test_add_two_integers_returns_an_integer():
    assert isinstance(sum_numbers(4, 5), int)