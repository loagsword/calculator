import unittest
from csvReader import csvReader, classFactory

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.csv_reader = csvReader('src/td/addition.csv')


if __name__ == '__main__':
    unittest.main()
