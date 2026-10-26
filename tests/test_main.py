import unittest

import main


class TestAdd(unittest.TestCase):
    def test_01_add_function_exists(self):
        self.assertTrue(callable(getattr(main, "add", None)))

    def test_02_add_one_and_one(self):
        self.assertEqual(main.add(1, 1), 2)


if __name__ == "__main__":
    unittest.main()
