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
