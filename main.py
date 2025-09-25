def fibonacci_rec(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована рекурсивно согласно
    формуле вычисления последовательности.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n == 1 or n == 2:
        return 1
    
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


def fibonacci_iter(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно с использованием
    массива для хранения вычисляемых данных.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """
    if n == 1 or n == 2:
        return 1

    fib = [0] * (n + 1)  # да, массив из нулей — символ нашей жизни
    fib[1] = 1
    fib[2] = 1

    for i in range(3, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]


def fibonacci(n: int) -> int:
    """Возвращает N-е число Фибоначчи. Реализована итеративно без использования массива.

    :param n: порядковый номер числа Фибоначчи
    :return: число Фибоначчи
    """

    fib_num_1 = 1
    fib_num_2 = 1

    for i in range(2, n):
        fib_num_i = fib_num_1 + fib_num_2
        fib_num_1 = fib_num_2
        fib_num_2 = fib_num_i

    return fib_num_2


def main():
    n = 35
    print(f"Вычисление {n} числа Фибоначчи рекурсивно:")
    print(fibonacci_rec(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно:")
    print(fibonacci_iter(n))

    print(f"\nВычисление {n} числа Фибоначчи итеративно без использования массива:")
    print(fibonacci(n))


if __name__ == "__main__":
    main()
