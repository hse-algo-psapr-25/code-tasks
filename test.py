import unittest

from main import ErrorMessages, Bounds, find_bounds


class TestSomeFunction(unittest.TestCase):

    def test_sample(self):
        """Проверяет что-то ..."""
        self.assertIsNone(find_bounds(None, None))


if __name__ == "__main__":
    unittest.main()
