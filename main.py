import math

STR_LENGTH_ERROR_MSG = "Длина строки должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def _generate_strings_ending_in_zero(length: int) -> list[str]:

    if length == 1:
        return ["0"]
    return [s + "0" for s in _generate_strings_ending_in_one(length - 1)]


def _generate_strings_ending_in_one(length: int) -> list[str]:

    if length == 1:
        return ["1"]
    return [s + "1" for s in generate_strings(length - 1)]


def generate_strings(length: int) -> list[str]:
    
    if type(length) is not int or length <= 0:
        raise ValueError(STR_LENGTH_ERROR_MSG)

    if length == 1:
        return ["0", "1"]

    return _generate_strings_ending_in_zero(length) + _generate_strings_ending_in_one(length)


def _binomial_coefficient_recursive(n: int, k: int) -> int:

    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return _binomial_coefficient_recursive(n - 1, k - 1) + _binomial_coefficient_recursive(n - 1, k)


def _binomial_coefficient_iterative(n: int, k: int) -> int:

    if k < 0 or k > n:
        return 0
    if k > n // 2:
        k = n - k
    
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    return c


def binomial_coefficient(n: int, k: int, use_rec=False) -> int:

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

    if use_rec:
        return _binomial_coefficient_recursive(n, k)
    else:
        return _binomial_coefficient_iterative(n, k)


def main():
    n = 4
    print(f"Строки длиной {n}:\n{sorted(generate_strings(n))}")

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