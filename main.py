PATH_LENGTH_ERROR_MSG = "Длина маршрута должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина маршрута"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def get_triangle_path_count(length: int) -> int:
    """Вычисляет количество замкнутых маршрутов заданной длины между тремя
    вершинами треугольника A, B и C. Маршруты начинаются и оканчиваются в
    вершине A vertex. Допустимыми являются все пути между различными вершинами.
    :param length: Длина маршрута.
    :raise ValueError: Если длина маршрута не является целым положительным
    числом.
    :return: Количество маршрутов.
    """

    if not isinstance(length, int) or isinstance(length, bool) or length <= 0:
        raise ValueError(PATH_LENGTH_ERROR_MSG)

    def a(n):
        if n == 1:
            return 0
        return b(n - 1) + c(n - 1)

    def b(n):
        if n == 1:
            return 1
        return a(n - 1) + c(n - 1)

    def c(n):
        if n == 1:
            return 1
        return a(n - 1) + b(n - 1)

    return a(length)

    # Укороченный вариант (сложнее для понимания, но кажется интереснее сам в себе)
    # (может быть не применим, для случаев, когда из разных точек разное число дорог)
    # def start_point(n):
    #
    #     def other_point(k):
    #         return 1 if k == 1 else start_point(k - 1) + other_point(k - 1)
    #     return 0 if n == 1 else other_point(n - 1) * 2
    #
    # return start_point(length)

def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """

    for name, value in [("n", n), ("k", k)]:
        if not isinstance(value, int) or isinstance(value, bool):
            raise ValueError(NOT_INT_VALUE_TEMPL.format(name))
        if value < 0:
            raise ValueError(NEGATIVE_VALUE_TEMPL.format(name))

    if n < k:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG)

    def rec_binom(n, k):
        if k == 0 or k == n:
            return 1
        return int(n / k * rec_binom(n - 1, k - 1))

    def iter_binom(n, k):
        if k == 0 or k == n:
            return 1
        res = 1
        for i in range(1, min(k, n - k) + 1):
            res = res * (n - i + 1) // i
        return res

    return rec_binom(n, k) if use_rec else iter_binom(n, k)


def main():
    n = 10
    print(f"Количество маршрутов длиной {n} = {get_triangle_path_count(n)}")

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
