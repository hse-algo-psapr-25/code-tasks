STR_LENGTH_ERROR_MSG = "Длина строки должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина строки"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""

def validate_length(length: int) -> None:
    """Валидирует длину строки на корректность

    :param length: Длина строки.
    :raise ValueError: Если длина строки не является целым положительным числом.
    """
    if not isinstance(length, int) or length <= 0 or isinstance(length, bool):
        raise ValueError(STR_LENGTH_ERROR_MSG)


def validate_parmas(n: int, k: int):
    """Валидирует параметры для биномиальных коэфициентов

    :param n: Из какого числа осуществляется выборка
    :param k: Сколько элементов надо выбрать из числа n
    :raise ValueError: Параметры не валидны
    """
    if not isinstance(n, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("n"))
    if not isinstance(k, int):
        raise ValueError(NOT_INT_VALUE_TEMPL.format("k"))
    if n < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("n"))
    if k < 0:
        raise ValueError(NEGATIVE_VALUE_TEMPL.format("k"))
    if n < k:
        raise ValueError(N_LESS_THAN_K_ERROR_MSG.format("n"))


def input_zero(length: int, string: str, result: list):
    """Процедура дописывающая ноль в существующую строку
    :param length: Длина строки.
    :param string: Текущая заполняемая строка
    :param result: Дополняемый строкой список
    """
    if length == 0:
        return
    string += '0'
    input_one(length - 1, string, result)


def input_one(length: int, string: str, result: list):
    """Процедура дописывающая единицу в существующую строку и обновляющая список строк
    :param length: Длина строки.
    :param string: Текущая заполняемая строка
    :param result: Дополняемый строкой список
    """
    if length == 0: 
        result.append(string)
        return
    string += '1'
    input_one(length - 1, string, result)
    input_zero(length - 1, string, result)


def generate_strings(length: int) -> list[str]:
    """Возвращает строки заданной длины, состоящие из 0 и 1, где никакие
    два нуля не стоят рядом.
    :param length: Длина строки.
    :raise ValueError: Если длина строки не является целым положительным
    числом.
    :return: Список строк.
    """
    validate_length(length)
    result = []
    input_zero(length, '', result)
    input_one(length, '', result)
    return result

def binomial_coefficient(n: int, k: int, use_rec=False) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :param use_rec: Использовать итеративную или рекурсивную реализацию функции.
    :raise ValueError: Если параметры не являются целыми неотрицательными
    числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    validate_parmas(n, k)
    
    if use_rec:
        return _binomial_coefficient_rec(n, k)
    return _binomial_coefficient_iter(n, k)
<<<<<<< HEAD
=======


def _binomial_coefficient_iter(n: int, k: int) -> int:
    """Итеративная реализация подсчета биномиальных коэфициентов

    Args:
        n (int): число элементов
        k (int): число элементов для выбора 

    Returns:
        int: значение биномиального коэфициента C(n, k)
    """
    if k == 1 or k == 1:
        return 1
    
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0] = [1] * (n + 1)
    
    for i in range(1, k + 1):
        for j in range(i, n + 1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    
    return dp[k][n-1] + dp[k-1][n-1]
>>>>>>> 40921eb (Fixes according to comments)


def _binomial_coefficient_rec(n: int, k: int) -> int:
    """Вычисляет биномиальный коэффициент из n по k.
    :param n: Количество элементов в множестве, из которого производится выбор.
    :param k: Количество элементов, которые нужно выбрать.
    :raise ValueError: Если параметры не являются целыми неотрицательными числами или значение параметра n меньше чем k.
    :return: Значение биномиального коэффициента.
    """
    if k == 0 or n == k:
        return 1
    
    return _binomial_coefficient_rec(n - 1, k) + _binomial_coefficient_rec(n - 1, k - 1)

def _binomial_coefficient_iter(n: int, k: int) -> int:
    """Итеративно вычисляет значение биномиального коэфициента

    Args:
        n (int): общее число элементов
        k (int): число элементов для выбора

    Returns:
        int: значение биномиального коэфициента
    """
    if k == 0 or k == n:
        return 1
    
    dp = [[0] * (n + 1) for _ in range(k + 1)]
    dp[0] = [1] * (n + 1)
    
    for i in range(1, k + 1):
        for j in range(i, n + 1):
            dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
    
    return dp[k][n-1] + dp[k-1][n-1]


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