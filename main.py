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
LevelResult = namedtuple("LevelResult", ["profit", "distributions"])


class ProfitValueError(Exception):
    def __init__(self, message, project_idx, row_idx):
        self.project_idx = project_idx
        self.row_idx = row_idx
        super().__init__(message)


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
    _validate_profit_matrix(profit_matrix)

    num_levels = len(profit_matrix)
    num_projects = len(profit_matrix[0])
    memo_table = [
        [LevelResult(profit=0, distributions=[]) for _ in range(num_levels)]
        for _ in range(num_projects)
    ]

    for project_idx in range(num_projects):
        for level_idx in range(num_levels):
            total_units = level_idx + 1

            if project_idx == 0:
                dist = [0] * num_projects
                dist[0] = total_units
                memo_table[project_idx][level_idx] = LevelResult(
                    profit=profit_matrix[level_idx][0],
                    distributions=[dist],
                )
                continue
            best_profit = 0
            best_distributions = []

            for units_prev, units_curr in _generate_distributions(total_units, 2):
                prev_profit = 0
                prev_LevelResult = None
                if units_prev > 0:
                    prev_LevelResult = memo_table[project_idx - 1][units_prev - 1]
                    prev_profit = prev_LevelResult.profit

                curr_profit = 0
                if units_curr > 0:
                    curr_profit = profit_matrix[units_curr - 1][project_idx]

                new_profit = prev_profit + curr_profit

                if new_profit > best_profit:
                    best_profit = new_profit
                    best_distributions = []

                    if units_prev == 0:
                        new_dist = [0] * num_projects
                        new_dist[project_idx] = units_curr
                        best_distributions.append(new_dist)
                    else:
                        for prev_dist in prev_LevelResult.distributions:
                            new_dist = list(prev_dist)
                            new_dist[project_idx] = units_curr
                            best_distributions.append(new_dist)

                elif new_profit == best_profit:
                    if units_prev == 0:
                        new_dist = [0] * num_projects
                        new_dist[project_idx] = units_curr
                        best_distributions.append(new_dist)
                    else:
                        for prev_dist in prev_LevelResult.distributions:
                            new_dist = list(prev_dist)
                            new_dist[project_idx] = units_curr
                            best_distributions.append(new_dist)

            memo_table[project_idx][level_idx] = LevelResult(
                profit=best_profit,
                distributions=best_distributions,
            )

    final_LevelResult = memo_table[-1][-1]
    return Result(profit=final_LevelResult.profit, distributions=final_LevelResult.distributions)

def _backtrack_distributions(remaining, boxes_left, current, result) :
    """
    Рекурсивная вспомогательная функция, собирает распределения в result.
    Не возвращает значение — добавляет кортежи в result.
    """
    if boxes_left == 1:
        result.append(tuple(current + [remaining]))
        return
    for i in range(remaining + 1):
        current.append(i)
        _backtrack_distributions(remaining - i, boxes_left - 1, current, result)
        current.pop()


def _generate_distributions(n, k):
    """
    Генерирует все способы распределения n одинаковых звёздочек по k коробочкам.
    Возвращает список кортежей длины k, где каждый элемент — количество звёзд в коробке.
    """
    if k == 0:
        return [] if n > 0 else [()]
    if n == 0:
        return [(0,) * k]

    result = []
    _backtrack_distributions(n, k, [], result)
    return result

def _validate_profit_matrix(profit_matrix: list[list[int]]) -> None:
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
