from problems.knapsack_problem.knapsack_abs_solver import (
    KnapsackAbstractSolver,
    KnapsackSolution,
)
from itertools import combinations


class BruteForceSolver(KnapsackAbstractSolver):
    def get_knapsack(self) -> KnapsackSolution:
        """
        Решает задачу о рюкзаке с использованием полного перебора.

        :return: максимально возможная общая стоимость и список индексов выбранных предметов
        :rtype: KnapsackSolution
        """
        _amount = len(self._weights)
        _best_cost: int = 0
        _best_items: list[int] = []

        # перебор всех комбинаций k предметов из n
        for k in range(_amount + 1):
            # все возможные комбинации для каждого количества k
            for comb in combinations(range(_amount), k):
                _selected_str = ''.join(
                    '1' if i in comb else '0' for i in range(_amount)
                    )
                _selected = [char == '1' for char in _selected_str]
                _current_weight = self.get_weight(_selected)
                if (
                    _current_weight <= self._weight_limit
                ):  # если есть место в рюкзаке...
                    _current_cost = self.get_cost(_selected)
                    if (
                        _current_cost > _best_cost and len(_selected) > 0
                    ):  # ...кладём предметы с макс. стоимостью
                        _best_cost = _current_cost
                        _best_items = [
                            item
                            for item, is_selected in enumerate(_selected)
                            if is_selected
                        ]
        return KnapsackSolution(cost=_best_cost, items=_best_items)


if __name__ == "__main__":
    weights = [11, 4, 8, 6, 3, 5, 5]
    costs = [17, 6, 11, 10, 5, 8, 6]
    weight_limit = 30
    print("Пример решения задачи о рюкзаке\n")
    print(f"Веса предметов для комплектования рюкзака: {weights}")
    print(f"Стоимости предметов для комплектования рюкзака: {costs}")
    print(f"Ограничение вместимости рюкзака: {weight_limit}")
    solver = BruteForceSolver(weights, costs, weight_limit)
    result = solver.get_knapsack()
    print(
        f"Максимальная стоимость: {result.cost}, " f"индексы предметов: {result.items}"
    )
