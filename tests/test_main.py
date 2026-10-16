import unittest
import main

from main import add

class TestAdd(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(3, 3), 6)
    def test_2(self):
        self.assertEqual(add(2, 2), 4)
    def test_3(self):
        self.assertEqual(add(1, 1), 2)
    def test_4(self):
        self.assertEqual(add(1, 0), 1)
    def test_5(self):
        self.assertEqual(add(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
