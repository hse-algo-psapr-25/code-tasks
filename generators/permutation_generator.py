from typing import Any

def validate_items(items: list[Any]):
    """
    Валидирует список элементов
    :param items: список элементов
    :raise TypeError: если параметр items не является списком
    :raise ValueError: если список элементов содержит дубликаты
    """
    if not isinstance(items, list):
        raise TypeError("Параметр items не является списком")
    if len(items) != len(set(items)):
        raise ValueError("Список элементов содержит дубликаты")

def generate_permutations(items: list[Any]) -> list[list[Any]]:
    """Генерирует все варианты перестановок элементов указанного множества

    :param items: список элементов
    :raise TypeError: если параметр items не является списком
    :raise ValueError: если список элементов содержит дубликаты
    :return: список перестановок, где каждая перестановка список элементов
    множества
    """
    try:
        validate_items(items)
        return _generate_permutations(items)
    except Exception as e:
        raise e

def _generate_permutations(items: list[Any]) -> list[list[Any]]:
    if (len(items) == 0):
        return []
    if len(items) == 1:
        return [items]

    perms = _generate_permutations(items[:-1])
    res = []
    last = items[-1]

    for p in perms:
        for i in range(len(items)):
            p_copy = p.copy()
            p_copy.insert(i, last)
            res.append(p_copy)

    return res


def main():
    items = [1, 2, 3]
    print(generate_permutations(items))


if __name__ == "__main__":
    main()
