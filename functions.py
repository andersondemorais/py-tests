# -*- coding: utf-8 -*-
# Using Python 3.x

"""
Functions to test with pytest
"""
__author__ = "Anderson Morais"
__copyright__ = "Copyright 2020"
__email__ = ""
__date__ = "12-may-2021"
__version__ = "0.1"
__status__ = ""


def ssum(number) -> int:
    if isinstance(number, int or float):
        return number + 4
    else:
        if number.isdigit():
            return int(number) + 4
    return 0


def prime_numbers(end: int) -> list:
    numbers = []
    for num in range(1, end + 1):
        if num != 1 and not any([num % div == 0 for div in range(2, num)]):
            numbers.append(num)
    return numbers


def convert_binary_to_decimal(binnary) -> int:
    decimal = 0

    if isinstance(binnary, int):
        binnary = str(binnary)

    if isinstance(binnary, str):
        if binnary.isnumeric():
            if all(elem in ["0", "1"] for elem in binnary):
                binnary = binnary[::-1]
                for exp in range(0, len(binnary)):
                    if binnary[exp] == "1":
                        decimal += pow(2, exp)

    return decimal


def convert_decimal_to_binary(decimal, complement: bool = False) -> str:
    binnary = ""
    qnt_bits = 8

    if isinstance(decimal, str):
        if decimal.isnumeric():
            decimal = int(decimal)
        else:
            return "0"

    if isinstance(decimal, int):
        if decimal > 255:
            qnt_bits = 16

        if decimal <= 65535:
            while decimal > 0:
                rest = decimal % 2
                decimal = decimal // 2

                if rest:
                    binnary += "1"
                else:
                    binnary += "0"

            binnary = binnary[::-1]
        else:
            return "0"

    if complement:
        binnary = binnary.rjust(qnt_bits, "0")

    return binnary


def x_range(end: int) -> list:
    return [x for x in xrange(end)]


def division_by_zero(number: int):
    return number / 0


def function_not_yet_implemented():
    pass
