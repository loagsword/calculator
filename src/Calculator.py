import calcOperations as calc


class Calculator():
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = calc.addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = calc.subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = calc.division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = calc.multiplication(a, b)
        return self.result

    def square(self, a):
        self.result = calc.square(a)
        return self.result

    def square_root(self, a):
        self.result = calc.square_root(a)
        return self.result
