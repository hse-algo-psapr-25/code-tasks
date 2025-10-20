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
    validate_matrix(profit_matrix)

    proj_cnt = len(profit_matrix[0])
    lvl_cnt = len(profit_matrix)

    ext_profit_matrix = [[0] * proj_cnt] + profit_matrix
    
    max_profits, back = get_max_profit(ext_profit_matrix)
    
    distributions = get_distributions(back, lvl_cnt, proj_cnt)

    return Result(profit=max_profits[lvl_cnt][proj_cnt - 1], distributions=distributions)


def validate_matrix(profit_matrix):
    if profit_matrix is None:
        raise ValueError(ErrorMessages.WRONG_MATRIX)
    
    if not profit_matrix:
        raise ValueError(ErrorMessages.WRONG_MATRIX)
    
    if not all(profit_matrix):
        raise ValueError(ErrorMessages.WRONG_MATRIX)
    
    row_lengths = [len(row) for row in profit_matrix]
    if len(set(row_lengths)) != 1:
        raise ValueError(ErrorMessages.WRONG_MATRIX)
    
    for row_idx, row in enumerate(profit_matrix):
        for col_idx, value in enumerate(row):
            if not isinstance(value, (int, float)):
                raise ValueError(ErrorMessages.WRONG_MATRIX)
    
    for col_idx in range(len(profit_matrix[0])):
        prev_value = -1
        for row_idx in range(len(profit_matrix)):
            current_value = profit_matrix[row_idx][col_idx]
            
            if current_value < 0:
                raise ProfitValueError(
                    ErrorMessages.NEG_PROFIT, 
                    col_idx,
                    row_idx
                )
            
            if current_value < prev_value:
                raise ProfitValueError(
                    ErrorMessages.DECR_PROFIT,
                    col_idx,
                    row_idx
                )
            
            prev_value = current_value

def get_max_profit(ext_profit_matrix):
    proj_cnt = len(ext_profit_matrix[0])
    lvl_cnt = len(ext_profit_matrix)

    max_profits = [[0] * proj_cnt for _ in range(lvl_cnt)]
    # Матрица для восстановления распределений
    # back[lvl][proj_idx] содержит список уровней инвестиций в проект, дающих максимальную прибыль
    back = [[[] for _ in range(proj_cnt)] for _ in range(lvl_cnt)]

    for lvl in range(lvl_cnt):
        max_profits[lvl][0] = ext_profit_matrix[lvl][0]
        back[lvl][0] = [lvl] # Все средства в первый проект

    for proj_idx in range(1, proj_cnt): # Для каждого проекта
        for lvl in range(lvl_cnt):      # Для каждого уровня инвестиций
            max_profit = 0
            max_profit_cur_proj = [] # Список распределений для проекта

            # Перебираем возможные инвестиции в проект
            for cur_lvl in range(lvl + 1):
                # prev_lvl - оставшиеся инвестиции для других проектов
                prev_lvl = lvl - cur_lvl
                # Прибыль от инвестиций cur_lvl в текущий проект
                current_profit = ext_profit_matrix[cur_lvl][proj_idx]
                # Максимальная прибыль от распределения prev_lvl
                prev_profit = max_profits[prev_lvl][proj_idx - 1]
                total_profit = current_profit + prev_profit
        
                if total_profit > max_profit:
                    max_profit = total_profit
                    max_profit_cur_proj = [cur_lvl] # Начинаем новый список распределений
                elif total_profit == max_profit:
                    max_profit_cur_proj.append(cur_lvl) # Добавляем альтернативное распределение
            
            max_profits[lvl][proj_idx] = max_profit
            back[lvl][proj_idx] = max_profit_cur_proj
    
    return max_profits, back


def get_distributions(back, lvl_cnt, proj_cnt):
    
    def backtrack(lvl, proj_idx, current_dist):
        # Базовый случай: дошли до первого проекта
        if proj_idx == 0:
            current_dist[proj_idx] = lvl # Все оставшиеся средства в первый проект
            distributions.append(current_dist.copy())
            return
        
        for i in back[lvl][proj_idx]:
            new_dist = current_dist.copy()
            new_dist[proj_idx] = i # Записываем инвестиции в текущий проект
            remaining = lvl - i # Вычисляем оставшиеся инвестии для следующих проектов
            backtrack(remaining, proj_idx - 1, new_dist)
    
    distributions = []
    initial_dist = [0] * proj_cnt
    backtrack(lvl_cnt, proj_cnt - 1, initial_dist)
    
    return distributions

def main():
    profit_matrix = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
    print(get_invest_distributions(profit_matrix))


if __name__ == "__main__":
    main()
