def fibonacci_rec(n: int) -> int:
    """
    Рекурсивная функция для нахождения n-го числа Фибоначчи.
    Базовые случаи: 1 и 2 → 1, иначе сумма двух предыдущих.
    """
    if n < 3:
        return 1
    return fibonacci_rec(n - 2) + fibonacci_rec(n - 1)


def fibonacci_iter(n: int) -> int:
    """
    Итеративная реализация через список.
    Формирует последовательность до нужного элемента.
    """
    if n <= 2:
        return 1
    fibs = [1, 1]
    for _ in range(2, n):
        fibs.append(fibs[-1] + fibs[-2])
    return fibs[-1]


def fibonacci(n: int) -> int:
    """
    Оптимизированная итеративная версия без списка.
    Использует только две переменные для хранения предыдущих значений.
    """
    if n <= 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))
