def check_strings(strings: list[str], target_string_length: int) -> bool:
    """Проверяет список строк содержит все строки заданной длины из нулей
    и единиц, где никакие два нуля не стоит рядом.

    param strings: Список строк для проверки.
    param target_string_length: Длина строки.

    return: Результат проверки.
    """
    pass


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
