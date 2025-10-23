import unittest

from main import ErrorMessages, SomeResult, some_function


class TestSomeFunction(unittest.TestCase):

    def test_sample(self):
        """Проверяет что-то ..."""
        self.assertIsNone(some_function(None, None))


if __name__ == "__main__":
    unittest.main()
