from typing import Dict, Tuple

STR_LENGTH_ERROR_MSG = "Длина строки должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def generate_strings(length: int) -> list[str]:
    """Возвращает строки заданной длины, состоящие из 0 и 1, где никакие
    два нуля не стоят рядом.

    :param length: Длина строки.
    :raise ValueError: Если длина строки не является целым положительным
    числом.
    :return: Список строк.
    """
    validate_len(length)
    strings = []
    add_one(length, strings, "")
    add_zero(length, strings, "")
    return strings


def validate_len(length: int) -> None:
    if not isinstance(length, int) or length < 1 or isinstance(length, bool):
        raise ValueError(STR_LENGTH_ERROR_MSG)


def add_zero(length, strings, string):
    string += "0"

    if len(string) == length:
        strings.append(string)
        return

    add_one(length, strings, string)


def add_one(length, strings, string):
    string += "1"

    if len(string) == length:
        strings.append(string)
        return

    add_one(length, strings, string)
    add_zero(length, strings, string)


def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    validate_binomial_coefs(n, k)

    if use_rec:
        return binomial_coefficient_rec(n, k)

    return binomial_coefficient_iter(n, k)


def validate_binomial_coefs(n: int, k: int):
    if not isinstance(n, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n"))
    if not isinstance(k, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("k"))

    if n < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n"))
    if k < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("k"))

    if n < k:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG)


def binomial_coefficient_rec(n: int, k: int) -> int:
    """
    Рекурсивно вычисляет биномиальный коэффициент C(n, k) по правилу Паскаля с кэшированием результатов
    """
    validate_binomial_coefs(n, k)

    if k == 0 or k == n:
        return 1

    k = min(k, n - k)

    from functools import lru_cache

    @lru_cache(maxsize=None)
    def c(nn: int, kk: int) -> int:
        if kk == 0 or kk == nn:
            return 1
        return c(nn - 1, kk) + c(nn - 1, kk - 1)

    return c(n, k)


def binomial_coefficient_iter(n: int, k: int) -> int:
    """Вычисляет биномиальный коэффициент из n по k
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :return: Значение биномиального коэффициента.
    """
    coefs = build_binomial_triangle(n, k)

    return coefs[(n, k)]


def build_binomial_triangle(rows: int, cols: int) -> Dict[Tuple[int, int], int]:
    """
    Строит нижнетреугольную матрицу, включая главную диагональ,
    используя словарь с картежом из двух значений ("координат") в качестве ключа
    и начального биноминальным коэфициентом в качестве значения
    :param rows: количество строк в матрице
    :param cols: количество колонок в матрице
    :return: нижнетреугольная матрица
    """
    coefs: Dict[Tuple[int, int], int] = {}
    for row_index in range(rows + 1):
        for col_index in range(cols + 1):
            if col_index > row_index:
                continue

            if col_index == 0 or col_index == row_index:
                coefs[(row_index, col_index)] = 1
                continue

            coefs[(row_index, col_index)] = coefs[(row_index - 1, col_index)] + coefs[(row_index - 1, col_index - 1)]

    return coefs


def main():
    n = 10
    print(f"Строки длиной {n}:\n{generate_strings(n)}")

    n = 30
    k = 20
    print(
        f"Биномиальный коэффициент (итеративно) при n, k ({n}, {k}) = ",
        binomial_coefficient_iter(n, k),
    )
    print(
        f"Биномиальный коэффициент (рекурсивно) при n, k ({n}, {k}) = ",
        binomial_coefficient_rec(n, k, use_rec=True),
    )


if __name__ == "__main__":
    main()
