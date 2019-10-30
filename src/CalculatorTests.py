import unittest
from Calculator import Calculator
from csvReader import CsvReader
from decimal import Decimal



class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.test_data = CsvReader('src/td/addition.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        self.test_data = CsvReader('src/td/subtraction.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_divide_method_calculator(self):
        self.test_data = CsvReader('src/td/division.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), Decimal(row['Result']))
            self.assertEqual(self.calculator.divide('0', row['Value 2']), 'error, the divisor can not be zero')

    def test_multiply_method_calculator(self):
        self.test_data = CsvReader('src/td/multiplication.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), Decimal(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_square_method_calculator(self):
        self.test_data = CsvReader('src/td/square.csv').data
        for row in self.test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), Decimal(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))


if __name__ == '__main__':
    unittest.main()
