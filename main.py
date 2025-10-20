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


Result = namedtuple("Result", ["profit", "distribution"])


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
    
    invest_count = len(profit_matrix)
    max_profit = [[0] * invest_count]


    max_profit = _get_max_profits(profit_matrix)

    distribution = _get_distribution(max_profit)
    return Result(profit=max_profit[-1][-1], distribution=distribution)

def _get_max_profits(profit_matrix):
    
    project_count = len(profit_matrix[0])
    extend_profit_matrix = [[0] * project_count] + profit_matrix
    project_cnt = len(extend_profit_matrix[0])
    level_cnt = len(extend_profit_matrix)

    max_profits = [[0] * project_cnt for _ in range(level_cnt)]
    
    for level in range(level_cnt):
        max_profits[level][0] = extend_profit_matrix[level][0]
        
    print(f"----------------------------НАЧАЛО---------------------------------")
    print(extend_profit_matrix)
    for proj_idx in range(project_cnt):
        for level in range(level_cnt):
            max_profit = 0
            max_profit_cur_level = 0
            print(f"Level: {level}")
            for cur_level in range(level+1):
                print(f"Cur Level: {cur_level}")
                prev_level = level - cur_level
                cur_profit = extend_profit_matrix[cur_level][proj_idx]
                prev_profit = max_profits[prev_level][proj_idx - 1]
                if cur_profit + prev_profit > max_profit:
                    max_profit = cur_profit + prev_profit
                    max_profit_cur_level = cur_level
            max_profits[level][proj_idx] = max_profit
            print(f"max_profits: {max_profits}")
            
    """
              А   AB   ABC   ABCD
        0:   [0,  0,   0,    0],
        100: [15, 18,  18,   18],
        200: [20, 33,  34,   35],
        300: [26, 38,  49,   51],
        400: [34, 44,  56,   66],
        500: [40, 52,  61,   73],
    """
    print(max_profits)
    return max_profits

def _get_distribution(costs):
    ...
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
