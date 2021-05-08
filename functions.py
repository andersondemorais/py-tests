def ssum(number):
    if isinstance(number, int or float):
        return number + 4
    else:
        if number.isdigit():
            return int(number) + 4
    return 0
