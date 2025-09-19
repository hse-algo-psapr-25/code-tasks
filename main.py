import time


def gcd_recursive(a: int, b: int) -> int:
    if type(a) != int  or type(b) != int:
        return "Нельзя не целые числа!"
    a, b = abs(a) , abs(b)
    if b == 0:
        return a
    return gcd_recursive(b, a % b)


def gcd_iterative_slow(a: int, b: int) -> int:
    if type(a) != int  or type(b) != int:
        return "Нельзя не целые числа!"
    a, b = abs(a) , abs(b)
    if a == 0:
        return b
    if b == 0:
        return a
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def gcd_iterative_fast(a: int, b: int) -> int:
    if type(a) != int  or type(b) != int:
        return "Нельзя не целые числа!"
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def lcm(a: int, b: int) -> int:
    if type(a) != int  or type(b) != int:
        return "Нельзя не целые числа!"
    a, b = abs(a) , abs(b)
    return a * b // gcd_iterative_fast(a, b)


def main():
    a = 100
    b = 1000
    print(f"Вычисление НОД чисел {a} и {b} рекурсивно:")
    start_time = time.time()
    print(gcd_recursive(a, b))
    print(f"Продолжительность: {time.time() - start_time} сек")

    print(f"\nВычисление НОД чисел {a} и {b} итеративно с вычитанием:")
    start_time = time.time()
    print(gcd_iterative_slow(a, b))
    print(f"Продолжительность: {time.time() - start_time} сек")

    print(f"\nВычисление НОД чисел {a} и {b} итеративно с делением:")
    start_time = time.time()
    print(gcd_iterative_fast(a, b))
    print(f"Продолжительность: {time.time() - start_time} сек")

    print(f"\nВычисление НОК чисел {a} и {b}:")
    start_time = time.time()
    print(lcm(a, b))
    print(f"Продолжительность: {time.time() - start_time} сек")


if __name__ == "__main__":
    main()
