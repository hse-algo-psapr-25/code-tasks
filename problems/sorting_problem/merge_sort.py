from typing import List, TypeVar, Optional, Union

T = TypeVar('T', int, float, str)


def validate_lst(lst: List[T]) -> None:
    """Валидирует список

    Args:
        lst (List[T]): список для проверки

    Raises:
        TypeError: если не список или элементы на сравнимы
        ValueError: передан пустой список
    """
    if not isinstance(lst, list):
        raise TypeError(f"Необходимо передать список, а не {type(lst).__name__}")
    if len(lst) == 0:
        raise ValueError(f'Список не может быть пустым для сортировки')
    
    first_elem = lst[0]
    for item in lst[1:]:
        try:
            _ = first_elem < item
        except TypeError:
            type1 = type(first_elem)
            type2 = type(item)
            
            if type1 == type2:
                raise TypeError(f"Переданы несравнимые экземпляры классов '{type2.__name__}' и '{type1.__name__}'")
            else:
                raise TypeError(f"Переданы несравнимые экземпляры классов '{type2.__name__}' и '{type1.__name__}'")


def merge_sort(lst: List[T], inplace: bool = False) -> Optional[List[T]]:
    """Универсальная сортировка слиянием с поддержкой inplace сортировки

    Args:
        lst (List[int]): сортируемый массив
        inplace (bool): флаг для вида сортировки

    Returns:
        Отсортированный массив или None если inplace сортировка
    """
    validate_lst(lst)
    
    if inplace:
        _merge_sort_inplace(lst, 0, len(lst))
        return None
    return _merge_sort_copy(lst)

def _merge_sort_copy(lst: List[T]) -> List[T]:
    """Сортировка слиянием обычная

    Args:
        lst (List[T]): сортируемый массив

    Returns:
        List[T]: отсортированный массив
    """
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = _merge_sort_copy(lst[:mid])
    right = _merge_sort_copy(lst[mid:])
    
    return _merge(left, right)

def _merge_sort_inplace(lst: List[T], start: int, end: int) -> None:
    """Сортировка слиянием inplace

    Args:
        lst (List[T]): исходный список
        start (int): индекс начала списка
        end (int): индекс конца списка
    """
    if end - start <= 1:
        return
    
    mid = (start + end) // 2
    _merge_sort_inplace(lst, start, mid)
    _merge_sort_inplace(lst, mid, end)
    _merge_inplace(lst, start, mid, end)

def _merge(left: List[T], right: List[T]) -> List[T]:
    """Слияние для обычный сортировки

    Args:
        left (List[T]): левая часть списка
        right (List[T]): правая часть списка

    Returns:
        result (List[T]): подмассив с отсортированными значениями
    """
    result = []
    idx_left, idx_right = 0, 0
    
    while idx_left < len(left) and idx_right < len(right):
        if left[idx_left] < right[idx_right]:
            result.append(left[idx_left])
            idx_left += 1
        else:
            result.append(right[idx_right])
            idx_right += 1
    
    result.extend(left[idx_left:])
    result.extend(right[idx_right:])
    return result


def _merge_inplace(lst: List[T], start: int, mid: int, end: int) -> None:
    """Слияние inplace (в исходном списке)

    Args:
        lst (List[T]): исходный список
        start (int): индекс начала списка
        mid (int): индекс середины списка
        end (int): индекс конца списка
    """
    left = lst[start:mid]
    right = lst[mid:end]
    
    idx_left, idx_right = 0, 0
    idx_lst = start
    
    while idx_left < len(left) and idx_right < len(right):
        if left[idx_left] < right[idx_right]:
            lst[idx_lst] = left[idx_left]
            idx_left += 1
        else:
            lst[idx_lst] = right[idx_right]
            idx_right += 1
        idx_lst += 1
    
    while idx_left < len(left):
        lst[idx_lst] = left[idx_left]
        idx_left += 1
        idx_lst += 1

    while idx_right < len(right):
        lst[idx_lst] = right[idx_right]
        idx_right += 1
        idx_lst += 1


def main():
    print("Пример сортировки ...")
    items = [5, 8, 1, 4, -7, 6, 12, 19, -6]
    items_copy1 = items.copy()
    items_copy2 = items.copy()
    print(f"Исходный массив: {items}")
    print(f"Отсортированный массив: {merge_sort(items_copy1)}")
    merge_sort(items_copy2, inplace=True)
    print(f"Отсортированный массив inplace: {items_copy2}")


if __name__ == "__main__":
    main()
