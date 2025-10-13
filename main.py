PATH_LENGTH_ERROR_MSG = "Длина маршрута должна быть целым положительным числом"
"""Сообщение об ошибке при некорректном значении параметра Длина маршрута"""

NOT_INT_VALUE_TEMPL = "Параметр {0} Не является целым числом"
"""Шаблон сообщения об ошибке при нечисловом значении параметра"""

NEGATIVE_VALUE_TEMPL = "Параметр {0} отрицательный"
"""Шаблон сообщения об ошибке при отрицательном значении параметра"""

N_LESS_THAN_K_ERROR_MSG = "Параметр n меньше чем k"
"""Сообщение об ошибке при значении параметра n меньше чем k"""


def get_triangle_path_count(length: int) -> int:
    if not isinstance(length, int) or length <= 0 or length is True:
        raise ValueError(PATH_LENGTH_ERROR_MSG)
    return _a(length)


def _a(n:int) -> int:
    #Не существует пути от А до А длиной 1, возьмем за базу рекурсии
    if n == 1:
        return 0
    return _b(n-1) + _c(n-1)

def _b(n:int) ->int:
    #Минимальный путь от А до B длиной один существует и единственнен, он и будет базой
    if n == 1:
        return 1
    return _a(n-1) + _c(n-1)


def _c(n:int) ->int:
    #Минимальный путь от А до С длиной один существует и единственнен
    if n == 1:
        return 1
    return _b(n-1) + _a(n-1)

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
        return binom_rec(n, k)
    else:
        return binom_iter(n, k)

def binom_rec(n,k) -> int:
    if (k == 0) or (k == n):
        return 1
    return int(n / k * binom_rec(n-1, k-1))

def binom_iter(n,k) -> int:
    
    if (k == 0) or (k == n):
        return 1
    koeffs = [[1] * (k+1) for _ in range (n +1) ]
    for row_indx in range(1, n+ 1):
        for col_indx in range(1, k + 1):
            if row_indx > col_indx:
                koeffs[row_indx][col_indx] =  koeffs[row_indx -1][col_indx -1] + koeffs[row_indx -1][col_indx]
    
    return koeffs[n][k]
    

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
