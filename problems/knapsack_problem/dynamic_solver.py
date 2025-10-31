from problems.knapsack_problem.knapsack_abs_solver import (
    KnapsackAbstractSolver,
    KnapsackSolution,
)


class DynamicSolver(KnapsackAbstractSolver):
    def get_knapsack(self) -> KnapsackSolution:
        """
        Решает задачу о рюкзаке с использованием метода динамического программирования.

        :return: максимально возможная общая стоимость и список индексов выбранных предметов
        :rtype: KnapsackSolution
        """
        solution_matrix = [[]] * (self.item_cnt + 1)
        for i in range(0, len(solution_matrix)):
            solution_matrix[i] = [0] * (self.weight_limit + 1)

        for i in range(0, self.item_cnt):
            item_cost = self.costs[i]
            item_weight = self.weights[i]
            item_idx = i + 1
            for weight in range(1, self.weight_limit + 1):
                if(item_weight > weight):
                    solution_matrix[item_idx][weight] = solution_matrix[item_idx - 1][weight]
                    continue
                solution_matrix[item_idx][weight] = max(
                    solution_matrix[item_idx - 1][weight],
                    solution_matrix[item_idx - 1][weight - item_weight] + item_cost
                )

        total_cost = solution_matrix[self.item_cnt][self.weight_limit]
        if total_cost == 0:
            return KnapsackSolution(cost=0, items=[])
        
        items = []
        weight_limit = self.weight_limit
        for i in range(self.item_cnt, 0, -1):
            if solution_matrix[i][weight_limit] != solution_matrix[i - 1][weight_limit]:
                weight_limit -= self.weights[i - 1]
                items.append(i - 1)
        return KnapsackSolution(cost=total_cost, items=items)


if __name__ == "__main__":
    weights = [11, 4, 8, 6, 3, 5, 5]
    costs = [17, 6, 11, 10, 5, 8, 6]
    weight_limit = 30
    print("Пример решения задачи о рюкзаке\n")
    print(f"Веса предметов для комплектования рюкзака: {weights}")
    print(f"Стоимости предметов для комплектования рюкзака: {costs}")
    print(f"Ограничение вместимости рюкзака: {weight_limit}")
    solver = DynamicSolver(weights, costs, weight_limit)
    result = solver.get_knapsack()
    print(
        f"Максимальная стоимость: {result.cost}, " f"индексы предметов: {result.items}"
    )
