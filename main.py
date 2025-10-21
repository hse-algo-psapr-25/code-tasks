from collections import namedtuple
from strenum import StrEnum


class ErrorMessages(StrEnum):
    """Перечисление сообщений об ошибках."""

    WRONG_MATRIX = (
        "Таблица прибыли от проектов не является прямоугольной "
        "матрицей с числовыми значениями"
    )
    NEG_PROFIT = "Значение прибыли не может быть отрицательно"
    DECR_PROFIT = "Значение прибыли не может убывать с ростом инвестиций"


Result = namedtuple("Result", ["profit", "distribution"])


class ProfitValueError(Exception):
    def __init__(self, message: str, project_idx: int, row_idx: int):
        self.project_idx = project_idx
        self.row_idx = row_idx
        super().__init__(message)

def get_invest_distribution(
    profit_matrix: list[list[int]],
) -> Result:
    """Рассчитывает максимально возможную прибыль и распределение инвестиций
    между несколькими проектами. Инвестиции распределяются кратными частями.

    :param profit_matrix: Таблица с распределением прибыли от проектов в
    зависимости от уровня инвестиций. Проекты указаны в столбцах, уровни
    инвестиций в строках.
    :raise ValueError: Если таблица прибыли от проектов не является
    прямоугольной матрицей с числовыми значениями.
    :raise ProfitValueError: Если значение прибыли отрицательно или убывает
    с ростом инвестиций.
    :return: именованный кортеж Result с полями:
    profit - максимально возможная прибыль от инвестиций,
    distribution - распределение инвестиций между проектами.
    """
    L, P = _validate_matrix(profit_matrix) #Валидация

    ext_profit = _build_extended_profit(profit_matrix, L, P) #расширение матрицы нулевой строкой и нулевым столбцом

    max_profits, choise = _get_max_profits(ext_profit) #посчитаем dp и choise

    distribution = _get_distribution(choise) #восстановим распределение

    return Result(profit = max_profits[L][P], distribution = distribution) #возварт максимума и распределения

def _is_number(x):
    return isinstance(x, (int, float))

def _validate_matrix(profit_matrix):
    if (
        profit_matrix is None
        or not isinstance(profit_matrix, list)
        or len(profit_matrix) == 0
        or not isinstance(profit_matrix[0], list)
        or len(profit_matrix[0]) == 0
    ):
        raise ValueError(ErrorMessages.WRONG_MATRIX)

    L = len(profit_matrix) #количество строк
    P = len(profit_matrix[0]) #количество столбцов

    for i in range(L):
        row = profit_matrix[i]
        if not isinstance(row, list) or len(row) != P:
            raise ValueError(ErrorMessages.WRONG_MATRIX)
        for j in range(P):
            row_value = row[j]
            if row_value is None or not _is_number(row_value):
                raise ValueError(ErrorMessages.WRONG_MATRIX)
            if row_value < 0:
                raise ProfitValueError(ErrorMessages.NEG_PROFIT, project_idx=j, row_idx=i)

    for j in range(P):
        prev = profit_matrix[0][j]
        for i in range(1, L):
            cur = profit_matrix[i][j]
            if cur < prev:
                raise ProfitValueError(ErrorMessages.DECR_PROFIT, project_idx=j, row_idx=i)
            prev = cur

    return L, P

def _build_extended_profit(profit_matrix, L, P):
    ext = [[0] * (P + 1) for _ in range(L + 1)]

    for l in range(1, L + 1):
        for p in range(1, P + 1):
            ext[l][p] = profit_matrix[l - 1][p - 1]
    return ext


def _get_max_profits(ext_profit_matrix):
    L_plus_1 = len(ext_profit_matrix) #это матрица с добавленной нулевой строкой
    P_plus_1 = len(ext_profit_matrix[0])

    dp = [[0] * P_plus_1 for _ in range(L_plus_1)]
    choice = [[0] * P_plus_1 for _ in range(L_plus_1)]

    for proj in range(1, P_plus_1):
        for level in range(0, L_plus_1):
            best = None
            best_cur = 0
            for cur in range(0, level + 1):  # сколько дать текущему проекту
                candidate = dp[level - cur][proj - 1] + ext_profit_matrix[cur][proj]
                if (best is None) or (candidate > best):
                    best = candidate
                    best_cur = cur
            dp[level][proj] = best if best is not None else 0
            choice[level][proj] = best_cur

    return dp, choice

def _get_distribution(choice):
    L_plus_1 = len(choice)
    P_plus_1 = len(choice[0])

    L = L_plus_1 - 1
    P = P_plus_1 - 1

    distribution = [0] * P
    level = L
    proj = P
    while proj > 0:
        cur = choice[level][proj]
        distribution[proj - 1] = cur
        level -= cur
        proj -= 1
    return distribution


def main() -> None:
    profit_matrix = [
        [15, 18, 16, 17],
        [20, 22, 23, 19],
        [26, 28, 27, 25],
        [34, 33, 29, 31],
        [40, 39, 41, 37],
    ]
    print(get_invest_distribution(profit_matrix))


if __name__ == "__main__":
    main()
