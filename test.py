import unittest

from strings_checker import check_strings
from main import generate_strings


class TestChecker(unittest.TestCase):
    """Тесты для функции, проверяющей генерацию строк из 0 и 1"""

    def test_with_generator(self):
        """Проверка списка строк, которые возвращает функция генератор"""

        for length in range(10):
            self.assertTrue(check_strings(generate_strings(length), length))

    def test_empty(self):
        """Проверка пустого списка строк"""
        target_string_length = 0
        strings_to_check = []
        self.assertTrue(check_strings(strings_to_check, target_string_length))

    def test_min_correct(self):
        """Проверка минимального корректного списка"""
        target_string_length = 1
        strings_to_check = ["0", "1"]
        self.assertTrue(check_strings(strings_to_check, target_string_length))

    def test_min_incorrect(self):
        """Проверка минимального некорректного списка"""
        target_string_length = 1
        strings_to_check = ["0"]
        self.assertTrue(check_strings(strings_to_check, target_string_length))


if __name__ == "__main__":
    unittest.main()
