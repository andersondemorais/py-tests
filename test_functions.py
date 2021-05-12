# -*- coding: utf-8 -*-
# Using Python 3.x

"""
Simple tests using Python pytest
"""
__author__ = "Anderson Morais"
__copyright__ = "Copyright 2020"
__email__ = ""
__date__ = "12-may-2021"
__version__ = "0.1"
__status__ = ""


import pytest
from functions import (
    ssum,
    prime_numbers,
    convert_binary_to_decimal,
    convert_decimal_to_binary,
    x_range,
    division_by_zero,
    function_not_yet_implemented,
    guess_numbers,
)
import sys

python2_only = pytest.mark.skipif(sys.version_info > (2, 7), reason="Requires Python2")
"""
During test function setup the condition (“sys.version_info > (2, 7)”) is checked. 
If it evaluates to True, the test function will be skipped with the specified reason.
"""


@pytest.fixture
def word():
    return "python"


def test_uppercase(word):
    assert word.upper() == "PYTHON"


def test_convert_to_int(word):
    with pytest.raises(ValueError):
        int(word) == 0


def test_function_ssum():
    assert ssum(4) == 8
    assert ssum("33") == 37
    assert ssum("a3i") == 0


def test_function_prime_numbers():
    assert 97 in prime_numbers(100)


def test_convert_binary_to_decimal():
    assert convert_binary_to_decimal("10001") == 17
    assert convert_binary_to_decimal("i0001") == 0
    assert convert_binary_to_decimal(101) == 5
    assert convert_binary_to_decimal(102) == 0
    assert convert_binary_to_decimal("20001") == 0


def test_function_convert_decimal_to_binary():
    assert convert_decimal_to_binary(210) == "11010010"
    assert convert_decimal_to_binary("310") == "100110110"
    assert convert_decimal_to_binary(-47, True) == "00000000"
    assert convert_decimal_to_binary("-98i") == "0"
    assert convert_decimal_to_binary("31094") == "111100101110110"
    assert convert_decimal_to_binary("65536") == "0"


@python2_only
def test_function_x_range():
    assert 3 in x_range(10)


# skipping a test because it fails
@pytest.mark.xfail
def test_function_division_by_zero():
    assert division_by_zero(1)


# skip a test without a condition -> optional reason
@pytest.mark.skip(reason="Not implemented")
def test_function_not_yet_implemented():
    assert function_not_yet_implemented()


# the @parametrize decorator defines two different (number,birth,age) tuples
# so that the test_guess_numbers function will run twice using them in turn
@pytest.mark.parametrize("number,birth,age", [(10, 1958, 63), (82, 1994, 27)])
def test_guess_numbers(number, birth, age):
    assert guess_numbers(number, birth) == (number, age)
