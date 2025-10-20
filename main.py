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
    level_cnt = len(profit_matrix)

    ext_profit_matrix = [[0] * project_cnt] + profit_matrix

    max_profits, back = _get_max_profits(ext_profit_matrix)
    distribution = _get_distribution(back)

    return Result(
        profit=max_profits[-1][-1],
        distribution=distribution,
    )


def _validate_matrix(profit_matrix: list[list[int]]):
    if (
        not profit_matrix
        or not isinstance(profit_matrix, list)
        or not profit_matrix[0]
        or not all(isinstance(row, list) for row in profit_matrix)
    ):
        raise ValueError(ErrorMessages.WRONG_MATRIX)

    row_len = len(profit_matrix[0])
    for i, row in enumerate(profit_matrix):
        if len(row) != row_len:
            raise ValueError(ErrorMessages.WRONG_MATRIX)
        for j, value in enumerate(row):
            if not isinstance(value, (int, float)):
                raise ValueError(ErrorMessages.WRONG_MATRIX)
            if value < 0:
                raise ProfitValueError(ErrorMessages.NEG_PROFIT, j, i)

  
    for j in range(row_len):
        for i in range(1, len(profit_matrix)):
            if profit_matrix[i][j] < profit_matrix[i - 1][j]:
                raise ProfitValueError(ErrorMessages.DECR_PROFIT, j, i)


def _get_max_profits(ext_profit_matrix):
    project_cnt = len(ext_profit_matrix[0])
    level_cnt = len(ext_profit_matrix)

    max_profits = [[0] * project_cnt for _ in range(level_cnt)]
    back = [[0] * project_cnt for _ in range(level_cnt)]

    for proj_idx in range(project_cnt):
        for level in range(1, level_cnt):
            max_profit = 0
            max_profit_cur_level = 0
            for cur_level in range(level + 1):
                prev_level = level - cur_level
                cur_profit = ext_profit_matrix[cur_level][proj_idx]
                prev_profit = 0
                if proj_idx > 0:
                    prev_profit = max_profits[prev_level][proj_idx - 1]
                total_profit = cur_profit + prev_profit
                if total_profit > max_profit:
                    max_profit = total_profit
                    max_profit_cur_level = cur_level
            max_profits[level][proj_idx] = max_profit
            back[level][proj_idx] = max_profit_cur_level

    return max_profits, back


def _get_distribution(back):
    level_cnt = len(back)
    project_cnt = len(back[0])

    distribution = [0] * project_cnt
    level = level_cnt - 1
    for proj_idx in range(project_cnt - 1, -1, -1):
        cur_level = back[level][proj_idx]
        distribution[proj_idx] = cur_level
        level -= cur_level
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
