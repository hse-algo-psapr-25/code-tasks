from collections import namedtuple

INF = float("inf")
PARAM_ERR_MSG = "Таблица цен не является прямоугольной матрицей с числовыми значениями"

Result = namedtuple("Result", ["cost", "path"])


def get_min_cost_path(price_table: list[list[int | float]]) -> Result:
    """Определяет минимальную стоимость пути от левого верхнего до правого нижнего угла.
    Перемещения разрешены только вправо и вниз.
    Возвращает именованный кортеж с итоговой стоимостью и списком координат пути.
    """
    if not _is_valid(price_table):
        raise ValueError(PARAM_ERR_MSG)

    dp = _build_dp(price_table)
    path = _trace_path(dp)

    return Result(cost=dp[-1][-1], path=path)


def _is_valid(table: list[list[int | float]]) -> bool:
    """Проверка таблицы на корректность и прямоугольность."""
    if not isinstance(table, list) or not table:
        return False

    cols = len(table[0])
    for row in table:
        if not isinstance(row, list) or len(row) != cols or not row:
            return False
        for val in row:
            if not isinstance(val, (int, float)) or isinstance(val, bool):
                return False
            if val in (float("inf"), float("-inf")) or (isinstance(val, float) and val != val):
                return False
    return True


def _build_dp(table: list[list[int | float]]) -> list[list[float]]:
    """Создаёт таблицу минимальных стоимостей с использованием динамического программирования."""
    rows, cols = len(table), len(table[0])
    dp = [[INF for _ in range(cols)] for _ in range(rows)]

    dp[0][0] = table[0][0]

    for i in range(rows):
        for j in range(cols):
            if i > 0:
                dp[i][j] = min(dp[i][j], dp[i - 1][j] + table[i][j])
            if j > 0:
                dp[i][j] = min(dp[i][j], dp[i][j - 1] + table[i][j])
    return dp


def _trace_path(dp: list[list[float]]) -> list[tuple[int, int]]:
    """Восстанавливает маршрут минимальной стоимости."""
    i, j = len(dp) - 1, len(dp[0]) - 1
    path = [(i, j)]

    while i > 0 or j > 0:
        if i == 0:
            j -= 1
        elif j == 0:
            i -= 1
        else:
            if dp[i - 1][j] < dp[i][j - 1]:
                i -= 1
            else:
                j -= 1
        path.append((i, j))

    return list(reversed(path))


def main():
    table = [[1, 2, 2], [3, 4, 2], [1, 1, 2]]
    print(get_min_cost_path(table))


if __name__ == "__main__":
    main()
