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
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_only_invalid_strings(self):
        """Все строки некорректны"""
        target_string_length = 2
        strings_to_check = ["00", "00", "000"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_empty_when_not_zero_length(self):
        """Пустой список для длины > 0"""
        target_string_length = 3
        strings_to_check = []
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_partial_overlap(self):
        """Список содержит неполный набор"""
        target_string_length = 3
        strings_to_check = ["101", "010", "110"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_all_zeros_invalid(self):
        """Строка полностью из нулей"""
        target_string_length = 3
        strings_to_check = ["000", "010", "101"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_two_zeros_together(self):
        """Строка с двумя нулями подряд"""
        target_string_length = 3
        strings_to_check = ["001", "010", "011"]  # "001" некорректна
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_non_unique_codes(self):
        """Проверка неуникальных кодов"""
        target_string_length = 3
        strings_to_check = ["101", "010", "101"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_invalid_length_codes(self):
        """Проверка кодов неправильной длины"""
        target_string_length = 3
        strings_to_check = ["1010", "010", "101"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_two_zeros_together_2(self):
        """Строка с двумя нулями подряд"""
        target_string_length = 3
        strings_to_check = ["001", "010", "100"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_partial_overlap_2(self):
        """Список содержит неполный набор"""
        target_string_length = 3
        strings_to_check = ["101", "010"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_non_unique_codes_2(self):
        """Проверка неуникальных кодов"""
        target_string_length = 4
        strings_to_check = ["1010", "0101", "1010"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_invalid_length_codes_3(self):
        """Проверка кодов неправильной длины для длины 4"""
        target_string_length = 4
        strings_to_check = ["10101", "0101", "1010"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_two_zeros_together_3(self):
        """Строка с двумя нулями подряд"""
        target_string_length = 4
        strings_to_check = ["0011", "0101", "1000"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

    def test_partial_overlap_3(self):
        """Список содержит неполный набор"""
        target_string_length = 4
        strings_to_check = ["1010", "0101"]
        self.assertFalse(check_strings(strings_to_check, target_string_length))

if __name__ == "__main__":
    unittest.main()
