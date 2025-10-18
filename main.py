from collections import namedtuple

# from strenum import StrEnum


# class ErrorMessages(StrEnum):
#     """Перечисление сообщений об ошибках."""

#     WRONG_MATRIX = (
#         "Таблица прибыли от проектов не является прямоугольной "
#         "матрицей с числовыми значениями"
#     )
#     NEG_PROFIT = "Значение прибыли не может быть отрицательно"
#     DECR_PROFIT = "Значение прибыли не может убывать с ростом инвестиций"


# Result = namedtuple("Result", ["profit", "distribution"])


# class ProfitValueError(Exception):
#     def __init__(self, message, project_idx, row_idx):
#         self.project_idx = project_idx
#         self.row_idx = row_idx
#         super().__init__(message)


def get_invest_distribution(
    profit_matrix: list[list[int]],
):
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
    project_count = len(profit_matrix[0])
    invest_count = len(profit_matrix)
    dp = [[0] * project_count for _ in range(invest_count + 1)]
    
    prev_dp = [[0] * project_count for _ in range(invest_count + 1)]
    
    for project_idx in range(project_count):
        dp[0][project_idx] = 0
        prev_dp[0][project_idx] = 0
    """
              А   B   C   D
        100: [15, 18, 16, 17],
        200: [20, 22, 23, 19],
        300: [26, 28, 27, 25],
        400: [34, 33, 29, 31],
        500: [40, 39, 41, 37],

        AB:
        Варианты распределения 1:
        1-1 = 15
        1-2 = 18
        Варианты распределения 2:
        2-1 = 20
        2-2 = 22
        1-1 + 1-2 = 15 + 18
        Варианты распределения 3:
        3-1 = 26
        3-2 = 28
        1-1 + 2-2 = 15 + 22
        2-1 + 1-2 = 20 + 18
    """
    for project_idx in range(project_count):
        for invest_idx in range(1, invest_count + 1):
            max_profit = 0
            for current_invest_idx in range(invest_idx):
                prev_invest = invest_idx - current_invest_idx
                
    
    return dp

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
