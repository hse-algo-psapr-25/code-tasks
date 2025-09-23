def fib(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def check_strings(strings: list[str], target_string_length: int) -> bool:
    """Проверяет список строк содержит все строки заданной длины из нулей
    и единиц, где никакие два нуля не стоит рядом.

    param strings: Список строк для проверки.
    param target_string_length: Длина строки.

    return: Результат проверки.
    """
    if target_string_length == 0 and strings == []:
        return True

    expected_count = fib(target_string_length + 2)
    if len(strings) != expected_count:
        return False

    seen = set()
    for s in strings:
        if len(s) != target_string_length:
            return False
        if "00" in s:
            return False
        if s in seen:
            return False
        seen.add(s)

    return True


def main():
    correct_strings = ["01", "10"]
    incorrect_strings = ["01", "10", "00"]

    print("Проверка корректного набора строк")
    print("Набор:")
    [print(string) for string in correct_strings]
    print(f"Результат проверки: {check_strings(correct_strings, 2)}")

    print("Проверка некорректного набора строк")
    print("Набор:")
    [print(string) for string in incorrect_strings]
    print(f"Результат проверки: {check_strings(incorrect_strings, 2)}")


if __name__ == "__main__":
    main()
