import unittest

import main


class TestAdd(unittest.TestCase):
    def test_01_add_function_exists(self):
        self.assertTrue(callable(getattr(main, "add", None)))

    def test_02_add_one_and_one(self):
        self.assertEqual(main.add(1, 1), 2)

    def test_03_add_one_and_two(self):
        self.assertEqual(main.add(1, 2), 3)

    def test_04_add_two_and_two(self):
        self.assertEqual(main.add(2, 2), 4)


class TestSubtract(unittest.TestCase):
    def test_05_subtract_one_and_one(self):
        self.assertEqual(main.subtract(1, 1), 0)

    def test_06_subtract_two_and_one(self):
        self.assertEqual(main.subtract(2, 1), 1)

    def test_07_subtract_one_and_two(self):
        self.assertEqual(main.subtract(1, 2), -1)


if __name__ == "__main__":
    unittest.main()
