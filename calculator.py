import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = self.calculator.subtract(10, 5)
        self.assertEqual(result, 5)

    def test_multiplication(self):
        result = self.calculator.multiply(2, 4)
        self.assertEqual(result, 8)

    def test_division(self):
        result = self.calculator.divide(10, 2)
        self.assertEqual(result, 5)

        # Test division by zero
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(5, 0)

if __name__ == '__main__':
    unittest.main()
