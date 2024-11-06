import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        # Display example output for addition
        print(f"Example: addition: {self.calc.add(1, 2)}")
        self.assertEqual(self.calc.add(1, 2), 3)

    def test_subtract(self):
        # Display example outputs for subtraction
        print(f"Example: subtraction: {self.calc.subtract(5, 3)}")
        print(f"Example: subtraction: {self.calc.subtract(3, 5)}")
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)

    def test_multiply(self):
        # Display example outputs for multiplication
        print(f"Example: multiplication: {self.calc.multiply(2, 3)}")
        print(f"Example: multiplication: {self.calc.multiply(-1, 3)}")
        self.assertEqual(self.calc.multiply(2, 3), 6)
        self.assertEqual(self.calc.multiply(-1, 3), -3)

    def test_divide(self):
        # Display example outputs for division
        print(f"Example: division: {self.calc.divide(6, 2)}")
        print(f"Example: division: {self.calc.divide(5, 2)}")
        self.assertEqual(self.calc.divide(6, 2), 3.0)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        
        # Check for division by zero
        with self.assertRaises(ZeroDivisionError):
            print(f"Example: division by zero: {self.calc.divide(5, 0)}")

if __name__ == '__main__':
    unittest.main(verbosity=2)

