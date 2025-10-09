from abc import ABC, abstractmethod
from collections import namedtuple

from problems.knapsack_problem.errors.constants import COSTS, WEIGHTS
from problems.knapsack_problem.errors.error_message_enum import ErrorMessageEnum
from problems.knapsack_problem.errors.error_message_template import (
    ErrorMessageTemplateEnum,
)

KnapsackSolution = namedtuple("KnapsackSolution", ["cost", "items"])


class KnapsackAbstractSolver(ABC):
    """Абстрактный класс для решения задачи о рюкзаке."""

    def __init__(self, weights: list[int], costs: list[int], weight_limit: int):
        """Создает объект класса для решения задачи о рюкзаке.

        :param weights: Список весов предметов для рюкзака.
        :param costs: Список стоимостей предметов для рюкзака.
        :param weight_limit: Ограничение вместимости рюкзака.
        :raise TypeError: Если веса или стоимости не являются списком с числовыми
        значениями, если ограничение вместимости не является целым числом.
        :raise ValueError: Если в списках присутствует нулевое или отрицательное
        значение.
        """
        self._validate_params(weights, costs, weight_limit)
        self._weights = weights
        self._costs = costs
        self._weight_limit = weight_limit

    @property
    def item_cnt(self):
        """Возвращает количество предметов для рюкзака."""
        return len(self._weights)

    @property
    def weights(self):
        """Возвращает список весов предметов для рюкзака."""
        return self._weights

    @property
    def costs(self):
        """Возвращает список стоимостей предметов для рюкзака."""
        return self._costs

    @property
    def weight_limit(self):
        """Возвращает ограничение вместимости рюкзака."""
        return self._weight_limit

    @abstractmethod
    def get_knapsack(self) -> KnapsackSolution:
        """Возвращает решение задачи о рюкзаке в виде именованного кортежа с полями:
        - cost - стоимость предметов в рюкзаке.
        - items - индексы предметов, добавленных в рюкзак.
        """
        pass

    def get_weight(self, selected_items: list[bool]) -> int:
        """Возвращает общий вес предметов, добавленных в рюкзак.

        :param selected_items: список логических значений, где для каждого предмета
        указано включен предмет в рюкзак или нет.
        """
        return sum(self._weights[i] for i in selected_items)

    def get_cost(self, selected_items: list[bool]) -> int:
        """Возвращает общую стоимость предметов, добавленных в рюкзак.

        :param selected_items: список логических значений, где для каждого предмета
        указано включен предмет в рюкзак или нет.
        """
        return sum(self._costs[i] for i in selected_items)

    def _validate_params(
        self, weights: list[int], costs: list[int], weight_limit: int
    ) -> None:
        """Проверяет входные данные задачи о рюкзаке.

        :param weights: Список весов предметов для рюкзака.
        :param costs: Список стоимостей предметов для рюкзака.
        :param weight_limit: Ограничение вместимости рюкзака.
        :raise TypeError: Если веса или стоимости не являются списком с числовыми
        значениями, если ограничение вместимости не является целым числом.
        :raise ValueError: Если в списках присутствует нулевое или отрицательное
        значение.
        """
        # проверка списков и типов элементов
        self._validate_list(weights, WEIGHTS)
        self._validate_list(costs, COSTS)

        # списки одинаковой длины
        if len(weights) != len(costs):
            raise ValueError(ErrorMessageEnum.LENGTHS_NOT_EQUAL)

        # элементы -- целые числа
        if not isinstance(weight_limit, int) or isinstance(weight_limit, bool):
            raise TypeError(ErrorMessageEnum.NOT_INT_WEIGHT_LIMIT)

        # значения элементов -- положительные
        if weight_limit <= 0:
            raise ValueError(ErrorMessageEnum.NOT_POS_WEIGHT_LIMIT)

        # минимальный вес предмета не больше ограничения по весу
        if weights and weight_limit < min(weights):
            raise ValueError(ErrorMessageEnum.LESS_WEIGHT_LIMIT)

    def _validate_list(self, items: list[int], list_name: str) -> None:
        """Проверяет список весов или список стоимостей в зависимости от параметра list_name"""

        if not isinstance(items, list):
            raise TypeError(ErrorMessageTemplateEnum.NOT_LIST)

        if len(items) == 0:
            raise ValueError(ErrorMessageTemplateEnum.EMPTY_LIST)

        for value in items:
            if not isinstance(value, int) or isinstance(value, bool):
                raise TypeError(ErrorMessageTemplateEnum.NOT_INT)
            if value <= 0:
                raise ValueError(ErrorMessageTemplateEnum.NOT_POS)
