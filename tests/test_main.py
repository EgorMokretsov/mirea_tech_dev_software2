import unittest
import main

from main import add, multiply


class TestAdd(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(3, 3), 6)

    def test_positive_numbers_2(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)

    def test_zero(self):
        self.assertEqual(add(7, 0), 7)


class TestMultiply(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_positive_numbers_2(self):
        self.assertEqual(multiply(3, 3), 9)

    def test_negative_number(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_zero(self):
        self.assertEqual(multiply(7, 0), 0)

class TestSubtract(unittest.TestCase):
    def test_subtract_positive_numbers(self):
        self.assertEqual(main.subtract(7, 3), 4)
    def test_negative_result(self):
        self.assertEqual(main.subtract(3, 7), -4)

    def test_subtract_zero(self):
        self.assertEqual(main.subtract(5, 0), 5)

class TestDivide(unittest.TestCase):
    def test_divide_positive_numbers(self):
        self.assertEqual(main.divide(8, 2), 4)
    def test_fractional_result(self):
        self.assertAlmostEqual(main.divide(7, 2), 3.5)

    def test_zero_numerator(self):
        self.assertEqual(main.divide(0, 5), 0)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            main.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
