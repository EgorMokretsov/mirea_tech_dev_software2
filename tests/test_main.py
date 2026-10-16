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

if __name__ == "__main__":
    unittest.main()
