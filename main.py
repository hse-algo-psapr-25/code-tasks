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


Result = namedtuple("Result", ["profit", "distributions"])


class ProfitValueError(Exception):
    def __init__(self, message, project_idx, row_idx):
        self.project_idx = project_idx
        self.row_idx = row_idx
        super().__init__(message)


def generate_distributions(n, k):
    """
    Генерирует все способы распределения n одинаковых звёздочек по k коробочкам.
    Возвращает список кортежей длины k, где каждый элемент — количество звёзд в коробке.
    """
    if k == 0:
        return [] if n > 0 else [()]
    if n == 0:
        return [(0,) * k]
    
    result = []
    def backtrack(remaining, boxes_left, current):
        if boxes_left == 1:
            result.append(tuple(current + [remaining]))
            return
        for i in range(remaining + 1):
            backtrack(remaining - i, boxes_left - 1, current + [i])

    backtrack(n, k, [])
    return result

def get_invest_distributions(
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
    distributions - списком со всеми вариантами распределения инвестиций между
    проектами, обеспечивающими максимальную прибыль.
    """
    
    if (
        not profit_matrix
        or not all(isinstance(row, list) and row for row in profit_matrix)
        or len({len(row) for row in profit_matrix}) != 1
        or not all(all(isinstance(x, (int, float)) for x in row) for row in profit_matrix)
    ):
        raise ValueError(ErrorMessages.WRONG_MATRIX)

    num_projects = len(profit_matrix[0])

    for project_idx in range(num_projects):
        prev_value = None
        for row_idx, row in enumerate(profit_matrix):
            value = row[project_idx]
            if value < 0:
                raise ProfitValueError(ErrorMessages.NEG_PROFIT, project_idx, row_idx)
            if prev_value is not None and value < prev_value:
                raise ProfitValueError(ErrorMessages.DECR_PROFIT, project_idx, row_idx)
            prev_value = value
    
    distributions = list()
    
    for i in range(len(profit_matrix[0])):
        distributions.append([[0, []] for _ in range(len(profit_matrix))])
        for j in range(len(profit_matrix)):
            if i == 0:
                new_distribution = [0] * len(profit_matrix[0])
                new_distribution[i] = j+1
                distributions[i][j] = [profit_matrix[j][0], [(new_distribution)]]
            else:
                max_profit = 0
                for k in generate_distributions(j+1, 2):
                    new_max_profit = 0
                    for x, y in enumerate(k):
                        if y == 0:
                            continue
                        if x == 0:
                            new_max_profit += distributions[i-1][y-1][0]
                        else:
                            new_max_profit += profit_matrix[y-1][i]
                    if new_max_profit == max_profit != 0:
                        if k[0] == 0:
                            new_distribution = [0] * len(profit_matrix[0])
                            new_distribution[i] = k[1]
                            distributions[i][j][1].append(new_distribution)
                        else:
                            for dist in distributions[i-1][k[0]-1][1]:
                                new_distribution = list(dist)
                                new_distribution[i] = k[1]
                                distributions[i][j][1].append(new_distribution)
                    elif new_max_profit > max_profit:
                        max_profit = new_max_profit
                        distributions[i][j][0] = max_profit
                        distributions[i][j][1] = []
                        if k[0] == 0:
                            new_distribution = [0] * len(profit_matrix[0])
                            new_distribution[i] = k[1]
                            distributions[i][j][1].append(new_distribution)
                        else:
                            for dist in distributions[i-1][k[0]-1][1]:
                                new_distribution = list(dist)
                                new_distribution[i] = k[1]
                                distributions[i][j][1].append(new_distribution)
   
    return Result(
        profit=distributions[-1][-1][0],
        distributions=distributions[-1][-1][1]
    )

def main():
    profit_matrix = [[8, 6, 6, 1, 4],
                     [15, 8, 9, 7, 8],
                     [16, 12, 13, 10, 14],
                     [19, 15, 17, 15, 16],
                     [20, 19, 19, 18, 21],
                     [25, 24, 24, 21, 22]]
    print(get_invest_distributions(profit_matrix))


if __name__ == "__main__":
    main()
