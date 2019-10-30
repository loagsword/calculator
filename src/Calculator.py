from decimal import Decimal


def addition(a, b):
    a = int(a)
    b = int(b)
    return a + b


def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c


def division(a, b):
    if int(a) != 0:
        a = Decimal(a)
        b = Decimal(b)
        c = b / a
        return round(c, 9)
    else:
        return 'error, the divisor can not be zero'


def multiplication(a, b):
    a = int(a)
    b = int(b)
    c = b * a
    return round(c, 9)


def square(a):
    a = int(a)
    c = a**2
    return c


def square_root(a):
    c = float('%.10g' % (int(a) ** (1/2)))
    return c


class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result
