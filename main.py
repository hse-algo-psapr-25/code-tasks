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
    _validate_length(length)

    strings = []
    _add_zero("", strings, length)
    _add_one("", strings, length)

    return strings


def _validate_length(length: int):
    # bool исключаем, 0 и отрицательные запрещаем
    if not isinstance(length, int) or isinstance(length, bool) or length < 1:
        raise ValueError(STR_LENGTH_ERROR_MSG)


def _add_zero(string: str, strings: list[str], length: int):
    """Добавляет '0' и вызывает _add_one (взаимная рекурсия)."""

    if len(string) == length - 1:
        strings.append(string + "0")
        return

    _add_one(string + "0", strings, length)


def _add_one(string: str, strings: list[str], length: int):
    """Добавляет '1' и вызывает обе функции."""
    if len(string) == length - 1:
        strings.append(string + "1")
        return

    _add_zero(string + "1", strings, length)
    _add_one(string + "1", strings, length)


def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    _validate_params(n, k)

    if use_rec:
        return binom_rec(n, k)
    return binom_iter(n, k)


def _validate_params(n, k):
    if not isinstance(n, int) or isinstance(n, bool):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n"))
    if not isinstance(k, int) or isinstance(k, bool):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("k"))

    if n < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n"))
    if k < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("k"))

    if n < k:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG)


def binom_rec(n, k):
    if k == 0 or k == n:
        return 1
    return binom_rec(n - 1, k) + binom_rec(n - 1, k - 1)


def binom_iter(n, k):
    if k == 0 or k == n:
        return 1
    coefficients = [[1] * (n + 1) for _ in range(n + 1)]

    for row_index in range(1, n + 1):
        for col_index in range(1, k + 1):
            if col_index < row_index:
                coefficients[row_index][col_index] = (
                    coefficients[row_index - 1][col_index]
                    + coefficients[row_index - 1][col_index - 1]
                )
    return coefficients[n][k]


def main():
    n = 2
    print(f"Строки длиной {n}:\n{generate_strings(n)}")

    n = 30
    k = 20
    print(
        f"Биномиальный коэффициент (итеративно) при n, k ({n}, {k}) = ",
        binomial_coefficient(n, k),
    )
    print(
        f"Биномиальный коэффициент (рекурсивно) при n, k ({n}, {k}) = ",
        binomial_coefficient(n, k, use_rec=True),
    )


if __name__ == "__main__":
    main()
