import random

from problems.sorting_problem.errors.error_message_template_enum import (
    ErrorMessageTemplateEnum,
)


def quick_sort(items):
    """
    Быстрая сортировка с рандомным опорным элементом (pivot)
    Возвращает новый список с отсортированными элементами по возрастанию

    Ошибка TypeError срабатывает если были встречены несравнимые элементы.
    Текст ошибки указан в файле error_message_template_enum.py

    Сложность алгоритма в худшем случае O(n^2)
    Примечание: благодаря random вероятность сложности O(n^2) становится очень маленькой
    """
    n = len(items)
    if n <= 1:
        return list(items)

    pivot = random.choice(items)  # рандомный опорный

    less, equal, greater = [], [], []
    for x in items:
        try:
            if x < pivot:
                less.append(x)
            elif x > pivot:
                greater.append(x)
            else:
                equal.append(x)
        except TypeError:

            raise TypeError(
                ErrorMessageTemplateEnum.ERR_INCOMPARABLE_EMBEDDED_TYPES.format(
                    type(pivot).__name__, type(x).__name__
                )
            )

    return quick_sort(less) + equal + quick_sort(greater)


def main():
    print("Пример сортировки ...")
    items = [5, 8, 1, 4, -7, 6, 12, 19, -6]
    print(f"Исходный массив: {items}")
    print(f"Отсортированный массив: {quick_sort(items)}")


if __name__ == "__main__":
    main()
