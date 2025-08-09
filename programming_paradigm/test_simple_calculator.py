import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        
        
    def test_subract(self):
        """Test the subtraction method."""
        
        self.assertEqual(self.calc.subtract(-1, 11), -12)
        
        
    def test_multiply(self):
        """Test the multiplication method."""
        
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        
    def test_divide(self):
        """Test the division method."""
        
        self.assertEqual(self.calc.divide(-1, 1), -1)
        
        self.assertEqual(self.calc.add(3, 3), 6)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-11, 1), -10)
        self.assertEqual(self.calc.subtract(-1, 1), -2)
        self.assertEqual(self.calc.multiply(-1, 1), -1)
        self.assertEqual(self.calc.multiply(11, 4), 44)
        self.assertEqual(self.calc.divide(-8, 1), -8)
        self.assertEqual(self.calc.divide(11, 11), 1)
        # Add more assertions to thoroughly test the add method.

# Remember to write additional test methods for subtract, multiply, and divide.