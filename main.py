from collections import namedtuple
from enum import StrEnum
from math import isnan


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
    def __init__(self, message, project_idx, row_idx):
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
    _validate_matrix(profit_matrix)

    project_cnt = len(profit_matrix[0])
    ext_profit_matrix = [[0] * project_cnt] + profit_matrix

    max_profits, back = _get_max_profits(ext_profit_matrix)
    distribution = _get_distribution(back)

    return Result(profit=max_profits[-1][-1], distribution=distribution)


def _validate_matrix(profit_matrix):
    if profit_matrix is None:
        raise ValueError(ErrorMessages.WRONG_MATRIX)
    if not isinstance(profit_matrix, list):
        raise ValueError(ErrorMessages.WRONG_MATRIX)
    if len(profit_matrix) == 0:
        raise ValueError(ErrorMessages.WRONG_MATRIX)

    for r in range(len(profit_matrix)):
        if not isinstance(profit_matrix[r], list):
            raise ValueError(ErrorMessages.WRONG_MATRIX)
        if len(profit_matrix[r]) == 0:
            raise ValueError(ErrorMessages.WRONG_MATRIX)

    row_len = len(profit_matrix[0])
    for r in range(len(profit_matrix)):
        if len(profit_matrix[r]) != row_len:
            raise ValueError(ErrorMessages.WRONG_MATRIX)

    for i in range(len(profit_matrix)):
        row = profit_matrix[i]
        for j in range(len(row)):
            val = row[j]
            if not isinstance(val, (int, float)):
                raise ValueError(ErrorMessages.WRONG_MATRIX)
            if isinstance(val, float) and isnan(val):
                raise ValueError(ErrorMessages.WRONG_MATRIX)
            if val < 0:
                raise ProfitValueError(ErrorMessages.NEG_PROFIT, j, i)

    rows = len(profit_matrix)
    cols = row_len
    for j in range(cols):
        for i in range(1, rows):
            if profit_matrix[i][j] < profit_matrix[i - 1][j]:
                raise ProfitValueError(ErrorMessages.DECR_PROFIT, j, i)

def _get_max_profits(ext_profit_matrix):
    project_cnt = len(ext_profit_matrix[0])
    level_cnt = len(ext_profit_matrix)

    max_profits = [[0] * project_cnt for _ in range(level_cnt)]
    back = [[0] * project_cnt for _ in range(level_cnt)]

    for level in range(level_cnt):
        max_profits[level][0] = ext_profit_matrix[level][0]
        back[level][0] = level

    for proj in range(1, project_cnt):
        for level in range(level_cnt):
            best_total = 0
            best_take = 0
            for take in range(level + 1):
                total = ext_profit_matrix[take][proj] + max_profits[level - take][proj - 1]
                if total > best_total:
                    best_total = total
                    best_take = take
            max_profits[level][proj] = best_total
            back[level][proj] = best_take

    return max_profits, back


def _get_distribution(back):
    total_levels = len(back) - 1
    project_cnt = len(back[0])
    distribution = [0] * project_cnt
    remaining = total_levels

    for proj in range(project_cnt - 1, 0, -1):
        take = back[remaining][proj]
        distribution[proj] = take
        remaining -= take

    distribution[0] = remaining
    return distribution


def main():
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
    