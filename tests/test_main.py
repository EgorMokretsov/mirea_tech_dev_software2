import unittest

import main


class TestAdd(unittest.TestCase):
    def test_01_add_function_exists(self):
        self.assertTrue(callable(getattr(main, "add", None)))


if __name__ == "__main__":
    unittest.main()
