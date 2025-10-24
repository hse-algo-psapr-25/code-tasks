from collections import namedtuple

from strenum import StrEnum

Bounds = namedtuple("Bounds", ["left_bound_less", "right_bound_more"])


class ErrorMessages(StrEnum):
    """Перечисление сообщений об ошибках."""

    PARAM_NOT_LIST = "Элемент не является списком"
    COMPARABLE_ERROR = "Элементы должны быть сравнимы"


def find_bounds(sorted_list: list, key) -> Bounds:
    """Возвращает диапазон индексов с заданным ключом в отсортированном списке sorted_list
    sorted_list: отсортированный список
    key: искомый ключ

    Returns:
        left_bound_less: индекс последнего элемента, который меньше ключа (-1, если ключа нет)
        right_bound_more: индекс последнего элемента, который больше ключа (len(sorted_list), если ключа нет)
    """
    ...


def main():
    """Примеры использования разрабатываемой функции"""
    find_bounds([1,2,3,3,4], 2) # (0, 2)
    find_bounds([1,2,3,3,4], 7) # (4, 5)
    find_bounds([1,2,3,3,4], 0) # (-1, 0)
    find_bounds([1], 2) # (1, 2)
    find_bounds([], 2) # (-1, 0)


if __name__ == "__main__":
    main()
