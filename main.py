PATH_LENGTH_ERROR_MSG = "Длина маршрута должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина маршрута"""

NOT_INT_VALUE_TEMPL = "Параметр {0} не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def get_triangle_path_count(length: int) -> int:
    """Вычисляет количество замкнутых маршрутов заданной длины между вершинами
    треугольника A, B и C. Путь начинается и заканчивается в A.
    :param length: Длина маршрута.
    :raise ValueError: Если длина маршрута не является целым положительным числом.
    :return: Количество маршрутов.
    """
    if isinstance(length, bool) or not isinstance(length, int) or length <= 0:
        raise ValueError(PATH_LENGTH_ERROR_MSG)

    def paths_from(vertex, n):
        """Рекурсивный подсчёт маршрутов из заданной вершины."""
        if n == 1:
            return 0 if vertex == "A" else 1
        if vertex == "A":
            return paths_from("B", n - 1) + paths_from("C", n - 1)
        elif vertex == "B":
            return paths_from("A", n - 1) + paths_from("C", n - 1)
        else:
            return paths_from("A", n - 1) + paths_from("B", n - 1)

    return paths_from("A", length)


def binomial_coefficient(n: int, k: int, use_rec: bool = False) -> int:
    """Вычисляет биномиальный коэффициент C(n, k).
    :param n: Общее количество элементов.
    :param k: Размер выборки.
    :param use_rec: Если True — использовать рекурсию, иначе итерацию.
    :raise ValueError: Если параметры заданы некорректно.
    :return: Значение биномиального коэффициента.
    """
    for name, val in (("n", n), ("k", k)):
        if isinstance(val, bool) or not isinstance(val, int):
            raise ValueError(NOT_INT_VALUE_TEMPL.format(name))
        if val < 0:
            raise ValueError(NEGATIVE_VALUE_TEMPL.format(name))

    if n < k:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG)

    if k == 0 or k == n:
        return 1

    if use_rec:
        prev = binomial_coefficient(n - 1, k - 1, use_rec=True)
        return (n * prev) // k

    if k > n - k:
        k = n - k
    coeff = 1
    for i in range(1, k + 1):
        coeff = coeff * (n - k + i) // i
    return coeff


def main():
    n = 10
    print(f"Количество маршрутов длиной {n}: {get_triangle_path_count(n)}")

    n, k = 30, 20
    print(f"C({n}, {k}) итеративно =", binomial_coefficient(n, k))
    print(f"C({n}, {k}) рекурсивно =", binomial_coefficient(n, k, use_rec=True))


if __name__ == "__main__":
    main()
