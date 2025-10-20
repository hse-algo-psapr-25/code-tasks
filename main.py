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


def _validate_profit_matrix(profit_matrix: list[list[int]]) -> None:
    """Валадирует входную матрицу

    Args:
        profit_matrix (list[list[int]]): матрица распредления прибыли от инвестиций

    Raises:
        Соответсвующие ошибки
    """
    if not profit_matrix:
        raise ValueError(ErrorMessages.WRONG_MATRIX)
    
    if not profit_matrix[0]:
        raise ValueError(ErrorMessages.WRONG_MATRIX)
    
    n_cols = len(profit_matrix[0])
    for i, row in enumerate(profit_matrix):
        if len(row) != n_cols:
            raise ValueError(ErrorMessages.WRONG_MATRIX)
        
        for j, value in enumerate(row):
            if not isinstance(value, (int, float)):
                raise ValueError(ErrorMessages.WRONG_MATRIX)
            if value < 0:
                raise ProfitValueError(ErrorMessages.NEG_PROFIT, j, i)
            
        if i > 0:
            for j in range(n_cols):
                if row[j] < profit_matrix[i-1][j]:
                    raise ProfitValueError(ErrorMessages.DECR_PROFIT, j, i)


def get_invest_distribution(profit_matrix: list[list[int]]):
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

    _validate_profit_matrix(profit_matrix)

    max_profit, choices = _get_max_profits(profit_matrix)
    distribution = _get_distribution(choices)
    
    return Result(profit=max_profit[-1][-1], distribution=distribution)


def _get_max_profits(profit_matrix: list[list[int]]) -> tuple[list[list[int]], list[list[int]]]:
    """Заполянет матрицу максимальной прибыли от вложений

    Args:
        profit_matrix (list[list[int]]): матрица прибыли от вложений

    Returns:
        tuple[list[list[int]], list[list[int]]]: матрица максимальной прибыли, матрица наших выборов для восстановления значения
    """
    n_projects = len(profit_matrix[0])
    invest_levels = len(profit_matrix)
    extend_matrix = [[0] * n_projects]
    extend_matrix.extend(profit_matrix)
    max_profits = [[0] * n_projects for _ in range(invest_levels + 1)]
    choices = [[0] * n_projects for _ in range(invest_levels + 1)]
    
    for investment in range(invest_levels + 1):
        max_profits[investment][0] = extend_matrix[investment][0]
        choices[investment][0] = investment
    
    for project in range(1, n_projects):
        for investment_level in range(invest_levels + 1):
            best_profit, best_choice = 0, 0
            for current_investment_level in range(investment_level + 1):
                prev_level = investment_level - current_investment_level
                prev_profit = max_profits[prev_level][project - 1]
                current_profit = extend_matrix[current_investment_level][project]
                current_total_profit = current_profit + prev_profit
                if current_total_profit > best_profit:
                    best_profit = current_total_profit
                    best_choice = current_investment_level
            max_profits[investment_level][project] = best_profit
            choices[investment_level][project] = best_choice
                
    return max_profits, choices
  
  
def _get_distribution(choices: list[list[int]]) -> list[int]:
    """восстанавливает наше решение (выборы проектов вложения)

    Args:
        choices (list[list[int]]): матрица наших выборов по проектам

    Returns:
        list[int]: список с вложениями, где на соответствующем индексе стоит сколько мы туда вложим частей нашего бюджета
    """
    n_projects = len(choices[0])
    total_investment = len(choices) - 1
    
    distribution = [0] * n_projects
    remaining_invest = total_investment
    
    for project in range(n_projects - 1, 0, -1):
        invest_to_proj = choices[remaining_invest][project]
        distribution[project] = invest_to_proj
        remaining_invest -= invest_to_proj
        
    distribution[0] = remaining_invest
    
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