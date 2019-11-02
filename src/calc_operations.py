from decimal import Decimal


def addition(a, b):
    return int(a) + int(b)


def subtraction(a, b):
    return int(b) - int(a)


def division(a, b):
    if int(a) != 0:
        return round((Decimal(b) / Decimal(a)), 9)
    else:
        return 'error, the divisor can not be zero'


def multiplication(a, b):
    return round((int(a) * int(b)), 9)


def square(a):
    return (int(a)) ** 2


def square_root(a):
    return float('%.10g' % (int(a) ** (1/2)))