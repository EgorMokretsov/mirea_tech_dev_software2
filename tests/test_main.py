import unittest
import main

from main import add

class TestAdd(unittest.TestCase):
    def test_1(self):
        self.assertEqual(add(3, 3), 6)

if __name__ == "__main__":
    unittest.main()
