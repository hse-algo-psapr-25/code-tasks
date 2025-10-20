from collections import namedtuple


INF = float("inf")
PARAM_ERR_MSG = "Таблица цен не является прямоугольной матрицей с числовыми значениями"

Result = namedtuple("Result", ["cost", "path"])


def get_min_cost_path(
    price_table: list[list[float | int]],
) -> Result:
    """Возвращает путь минимальной стоимости в таблице из левого верхнего угла
    в правый нижний. Каждая ячейка в таблице имеет цену посещения. Перемещение
    из ячейки в ячейку можно производить только по горизонтали вправо или по
    вертикали вниз.
    :param price_table: Таблица с ценой посещения для каждой ячейки.
    :raise ValueError: Если таблица цен не является прямоугольной матрицей с
    числовыми значениями.
    :return: Именованный кортеж Result с полями:
    cost - стоимость минимального пути,
    path - путь, список кортежей с индексами ячеек.
    """
    _validate(price_table)

    costs = _get_costs(price_table)
    path = _get_path(costs)

    return Result(cost=costs[-1][-1], path=path)


def _validate(price_table: list[list[float | int]]):
    # Таблица - непустой список списков
    if not isinstance(price_table, list) or not price_table:
        raise ValueError(PARAM_ERR_MSG)

    expected_len = None
    for row in price_table:
        if not isinstance(row, list) or not row:
            raise ValueError(PARAM_ERR_MSG)

        # Таблица прямоугольная
        if expected_len is None:
            expected_len = len(row)
            if expected_len == 0:
                raise ValueError(PARAM_ERR_MSG)
        elif len(row) != expected_len:
            raise ValueError(PARAM_ERR_MSG)

        # Значения корректны
        for val in row:
            # bool
            if isinstance(val, bool) or not isinstance(val, (int, float)):
                raise ValueError(PARAM_ERR_MSG)
            # NaN
            if isinstance(val, float) and val != val:
                raise ValueError(PARAM_ERR_MSG)
            # Бесконечности
            if val in (float("inf"), float("-inf")):
                raise ValueError(PARAM_ERR_MSG)


def _get_costs(price_table: list[list[float | int]]):
    costs = [[INF] * (len(price_table[0]) + 1) for _ in range(len(price_table) + 1)]
    costs[1][1] = price_table[0][0]

    for row_idx in range(1, len(costs)):
        for col_idx in range(1, len(costs[0])):
            if row_idx == 1 and col_idx == 1:
                continue
            costs[row_idx][col_idx] = price_table[row_idx - 1][col_idx - 1] + min(
                costs[row_idx - 1][col_idx], costs[row_idx][col_idx - 1]
            )
    return costs


def _get_path(costs_table: list[list[float | int]]):
    row_idx = len(costs_table) - 1
    col_idx = len(costs_table[0]) - 1
    path_back = [(row_idx - 1, col_idx - 1)]

    while row_idx > 1 or col_idx > 1:
        up_cost = costs_table[row_idx - 1][col_idx]
        left_cost = costs_table[row_idx][col_idx - 1]
        if up_cost < left_cost:
            row_idx -= 1
        else:
            col_idx -= 1
        path_back.append((row_idx - 1, col_idx - 1))

    return path_back[::-1]


def main():
    table = [[1, 2, 2], [3, 4, 2], [1, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == "__main__":
    main()
