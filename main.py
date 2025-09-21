def generate_strings(length: int) -> list[str]:
    """Возвращает строки заданной длины, состоящие из 0 и 1, где никакие
    два нуля не стоят рядом.

    :param length: Длина строки.
    :return: Список строк.
    """
    strings = []
    if length == 0:
        return strings

    for i in range(2**length):
        string = ("0" * length + str(bin(i))[2:])[-length:]
        if "00" not in string:
            strings.append(string)

    return strings


def main():
    n = 3
    print(f"Строки длиной {n}:")

    strings = generate_strings(n)
    print(f"Всего {len(strings)} строк:")
    for string in strings:
        print(string)


if __name__ == "__main__":
    main()
