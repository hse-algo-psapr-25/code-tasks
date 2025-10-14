from enum import StrEnum

PATH_LENGTH_ERROR_MSG = "Длина маршрута должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина маршрута"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""

class Vertex(StrEnum):
    A = 'A'
    B = 'B'
    C = 'C'

def get_triangle_path_count_for_vertex(length: int, vertex: Vertex) -> int:
    """Вспомогательная функция, рекурсивно вычисляет количество путей между
    вершинами треугольника.
    :param length: длина пути
    :param vertex: текущая вершина. Первый (нерекурсивный) вызов должен происходить
    для вершины А
    :raise ValueError: если вершина не равна A, B или C
    :return: Количество путей
    """
    if vertex == Vertex.A:
        if length == 0:
            return 1 # конец маршрута
        elif length < 2:
            return 0 # замкнутый маршрут невозможен
        return get_triangle_path_count_for_vertex(length - 1, Vertex.B) + get_triangle_path_count_for_vertex(length - 1, Vertex.C)
    elif vertex == Vertex.B or vertex == Vertex.C:
        otherVertex = Vertex.B if vertex == Vertex.C else Vertex.C
        if length == 0:
            return 0 # замкнутый маршрут невозможен
        elif length == 1:
            return 1 # можем пойти только в А и замкнуть маршрут
        return get_triangle_path_count_for_vertex(length - 1, Vertex.A) + get_triangle_path_count_for_vertex(length - 1, otherVertex)
    # никогда не должно происходить
    raise ValueError(f"invalid vertex: {vertex}")

def get_triangle_path_count(length: int) -> int:
    """Вычисляет количество замкнутых маршрутов заданной длины между тремя
    вершинами треугольника A, B и C. Маршруты начинаются и оканчиваются в
    вершине A vertex. Допустимыми являются все пути между различными вершинами.
    :param length: Длина маршрута.
    :raise ValueError: Если длина маршрута не является целым положительным
    числом.
    :return: Количество маршрутов.
    """
    if type(length) is not int or length <= 0:
        raise ValueError(PATH_LENGTH_ERROR_MSG)
    return get_triangle_path_count_for_vertex(length, Vertex.A)




def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    if type(n) is not int:
        raise ValueError(NOT_INT_VALUE_TEMPL.format('n'))
    elif n < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format('n'))
    if type(k) is not int:
        raise ValueError(NOT_INT_VALUE_TEMPL.format('k'))
    elif k < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format('k'))
    elif n < k:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG)
    if k == 0:
        return 1

    if use_rec:
        if k == 1:
            return n
        return binomial_coefficient(n - 1, k - 1, True) * n / k

    # итеративная ветвь
    result = 1
    for i in range(1, k + 1):
        result *= (n - k + i) / i

    return result



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
