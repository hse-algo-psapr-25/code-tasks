from typing import Optional, Tuple, List


class ErrorMessages:
    WRONG_COINS = "coins должен быть непустым списком положительных целых чисел"
    WRONG_AMOUNT = "amount должен быть неотрицательным целым числом"
    NEGATIVE_COIN = "монеты не могут быть отрицательными или нулевыми"


def validate_input(coins: List[int], amount: int) -> None:
    """
    Валидирует входные данные для задачи о размене монет.

    Args:
        coins: Список монет
        amount: Сумма для размена

    Raises:
        TypeError: Если тип данных некорректный
        ValueError: Если значения некорректные
    """
    if not isinstance(coins, list):
        raise TypeError("coins должен быть списком")
    if not isinstance(amount, int):
        raise TypeError("amount должен быть целым числом")
    if amount < 0:
        raise ValueError(ErrorMessages.WRONG_AMOUNT)
    if not coins:
        raise ValueError(ErrorMessages.WRONG_COINS)
    if any(not isinstance(coin, int) for coin in coins):
        raise TypeError("все монеты должны быть целыми числами")
    if any(coin <= 0 for coin in coins):
        raise ValueError(ErrorMessages.NEGATIVE_COIN)


def calculate_min_coins(coins: List[int], amount: int) -> Tuple[List[float], List[int]]:
    """
    Вычисляет минимальное количество монет для каждой суммы до amount.

    Args:
        coins: Список монет
        amount: Целевая сумма

    Returns:
        Кортеж (dp, coin_used), где:
        - dp: список минимального количества монет для каждой суммы
        - coin_used: список последних использованных монет для каждой суммы
    """
    dp = [float("inf")] * (amount + 1)
    coin_used = [-1] * (amount + 1)

    dp[0] = 0

    for summa in range(1, amount + 1):
        for coin in coins:
            if coin <= summa and dp[summa - coin] + 1 < dp[summa]:
                dp[summa] = dp[summa - coin] + 1
                coin_used[summa] = coin

    return dp, coin_used


def reconstruct_solution(coin_used: List[int], amount: int) -> List[int]:
    """
    Восстанавливает комбинацию монет по массиву использованных монет.

    Args:
        coin_used: Список последних использованных монет для каждой суммы
        amount: Целевая сумма

    Returns:
        Список монет, составляющих решение
    """
    combinations = []
    current_amount = amount

    while current_amount > 0:
        coin = coin_used[current_amount]
        if coin == -1:
            raise ValueError("Невозможно восстановить решение")
        combinations.append(coin)
        current_amount -= coin

    return combinations


def coin_change(coins: List[int], amount: int) -> Optional[Tuple[int, List[int]]]:
    """
    Основная функция для решения задачи о размене монет.

    Args:
        coins: Список доступных монет
        amount: Сумма для размена

    Returns:
        None если решение невозможно, иначе кортеж (количество_монет, комбинация)
    """
    validate_input(coins, amount)
    if amount == 0:
        return 0, []
    dp, coin_used = calculate_min_coins(coins, amount)

    if dp[amount] == float("inf"):
        return None

    combination = reconstruct_solution(coin_used, amount)

    return int(dp[amount]), combination


def main():
    amount = 13
    coins = [1, 2, 5]

    print("Пример решения задачи о размене монет\n")
    print(f"У нас имеется следующий набор монет: {coins}")
    print(f"Необходимо набрать сумму: {amount}")

    result = coin_change(coins, amount)

    if result:
        coin_need, coin_combination = result
        print(f"Необходимо: {coin_need} следующих монет {coin_combination}")
    else:
        print(f"Монетами: {coins} невозможно набрать сумму: {amount}")


if __name__ == "__main__":
    main()
