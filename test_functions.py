import pytest
from functions import (
    ssum,
    prime_numbers,
    convert_binary_to_decimal,
    convert_decimal_to_binary,
)


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
