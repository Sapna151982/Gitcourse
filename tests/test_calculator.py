import unittest
from calculator import add, subtract, multiply, divide

class TestCalculator(unittest.TestCase):
    def test_add(self):
        """Test the add function"""
        self.assertEqual(add(5, 3), 8)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        """Test the subtract function"""
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)
        self.assertEqual(subtract(0, 0), 0)

    def test_multiply(self):
        """Test the multiply function"""
        self.assertEqual(multiply(5, 3), 15)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        """Test the divide function"""
        self.assertEqual(divide(6, 2), 3)
        self.assertEqual(divide(-6, 2), -3)
        self.assertEqual(divide(-6, -2), 3)
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        """Test division by zero raises ValueError"""
        with self.assertRaises(ValueError):
            divide(5, 0)

if __name__ == '__main__':
    unittest.main()
