from problems.knapsack_problem.knapsack_abs_solver import (
    KnapsackAbstractSolver,
    KnapsackSolution,
)
from itertools import combinations


class BruteForceSolver(KnapsackAbstractSolver):
    def get_knapsack(self) -> KnapsackSolution:
        """
        Решает задачу о рюкзаке с использованием полного перебора.

        :return: максимальная возможнаая общая стоимость и список индексов выбранных предметов
        :rtype: KnapsackSolution
        """
        _n = len(self._weights)
        _best_cost: int = 0
        _best_items: list[int] = []

        # перебор всех комбинаций k предметов из n
        for k in range(_n + 1):
            # все возможные комбинации для каждого количества k
            for comb in combinations(range(_n), k):
                _items = list(comb)
                _weight = self.get_weight(_items)
                if _weight <= self._weight_limit:  # если есть место в рюкзаке...
                    _cost = self.get_cost(_items)
                    if (
                        _cost > _best_cost and len(_items) > 0
                    ):  # ...кладём предметы с макс. стоимостью
                        _best_cost = _cost
                        _best_items = _items

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
