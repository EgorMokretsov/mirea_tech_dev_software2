import unittest
import main

from main import add, multiply


class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_zero(self):
        self.assertEqual(add(7, 0), 7)


class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_negative_number(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_zero(self):
        self.assertEqual(multiply(7, 0), 0)

class TestSubtract(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(main.subtract(7, 3), 4)

class TestDivide(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(main.divide(8, 2), 4)

if __name__ == "__main__":
    unittest.main()
