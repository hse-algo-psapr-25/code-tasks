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

    # Валидация на типы
    if not profit_matrix or not isinstance(profit_matrix, list):
        raise ValueError(ErrorMessages.WRONG_MATRIX)
    if any(not isinstance(row, list) for row in profit_matrix):
        raise ValueError(ErrorMessages.WRONG_MATRIX)

    total_units = len(profit_matrix)
    row_len = len(profit_matrix[0])

    # Валидация корректность матрицы
    if total_units == 0:
        raise ValueError(ErrorMessages.WRONG_MATRIX)
    if row_len == 0:
        raise ValueError(ErrorMessages.WRONG_MATRIX)
    for row_index, row in enumerate(profit_matrix):
        if len(row) != row_len:
            raise ValueError(ErrorMessages.WRONG_MATRIX)
        for colum_index, val in enumerate(row):
            if not isinstance(val, (int, float)):
                raise ValueError(ErrorMessages.WRONG_MATRIX)
            if val < 0:
                raise ProfitValueError(ErrorMessages.NEG_PROFIT, colum_index, row_index)
            if row_index > 0:
                prev = profit_matrix[row_index - 1][colum_index]
                if val < prev:
                    raise ProfitValueError(ErrorMessages.DECR_PROFIT, colum_index, row_index)

    # Функционал
    NEG_INFINITY = float("-inf")
    result_prev = [NEG_INFINITY] * (total_units + 1)
    result_prev[0] = 0
    choices_path: list[list[int]] = []

    for left in range(row_len):
        result_curr = [NEG_INFINITY] * (total_units + 1)
        choice_path = [-1] * (total_units + 1)
        for count in range(0, total_units + 1):
            best_value = NEG_INFINITY
            best_path = 0
            for income in range(0, count + 1):
                prev_u = count - income
                prev_val = result_prev[prev_u]
                if prev_val == NEG_INFINITY:
                    continue
                add = 0
                if income > 0:
                    add = profit_matrix[income - 1][left]
                val = prev_val + add
                if val > best_value:
                    best_value = val
                    best_path = income
            result_curr[count] = best_value
            choice_path[count] = best_path
        result_prev = result_curr
        choices_path.append(choice_path)

    max_profit = result_prev[total_units]

    # восстановление распределения
    distribution = [0] * row_len
    rem = total_units
    for item in range(row_len - 1, -1, -1):
        choice_item = choices_path[item][rem]
        distribution[item] = choice_item
        rem -= choice_item

    return Result(int(max_profit), distribution)



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
