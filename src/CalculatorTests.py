import unittest
from Calculator import  Calculator
from CSVReader import CsvReader
#from pprint import pprint

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition_method_calculator(self):
       test_data = CsvReader('/src/Unit Test Addition.csv').data
       #pprint(test_data)
       for row in test_data:
           self.assertEqual(self.calculator.add(row['Value 1'],row['Value 2']),int(row['Result']))
           self.assertEqual(self.calculator.result,int(row['Result']))
       test_data.clear()

    def test_subtraction_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        #pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'],row['Value 2']),int(row['Result']))
            self.assertEqual(self.calculator.result,int(row['Result']))
        test_data.clear()

    def test_multiplication_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        #pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'],row['Value 2']),float(row['Result']))
            self.assertEqual(self.calculator.result,float(row['Result']))
        test_data.clear()

if __name__ == '__main__':
    unittest.main()