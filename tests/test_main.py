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
    def test_6(self):
        self.assertEqual(add(-1, 1), 0)
    def test_7(self):
        self.assertEqual(add(-2, 2), 0)
    def test_8(self):
        self.assertEqual(add(13, 3), 16)
    def test_9(self):
        self.assertEqual(add(133, 3), 136)
    def test_10(self):
        self.assertEqual(add(0, 3), 3)

if __name__ == "__main__":
    unittest.main()
