from typing import List, TypeVar, Optional

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
        return []


def merge_sort(lst: List[T], inplace: bool = False) -> Optional[List[T]]:
    """Сортировка слиянием, с предварительной валидацией списка

    Args:
        lst (List[int]): сортируемый массив
        inplace (bool): флаг для вида сортировки

    Returns:
        Отсортированный массив
        
    Raises:
        TypeError: если не список или элементы на сравнимы
        ValueError: передан пустой список
    """
    validate_lst(lst)
    
    return _merge_sort_copy(lst)

def _merge_sort_copy(lst: List[T]) -> List[T]:
    """Сортировка слиянием

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

def _merge(left: List[T], right: List[T]) -> List[T]:
    """Слияние для сортировки слиянием

    Args:
        left (List[T]): левая часть списка
        right (List[T]): правая часть списка

    Returns:
        result (List[T]): подмассив с отсортированными значениями
        
    Raises:
        TypeError: если элементы несравнимы
    """
    result = []
    idx_left, idx_right = 0, 0
    
    while idx_left < len(left) and idx_right < len(right):
        try:
            if left[idx_left] < right[idx_right]:
                result.append(left[idx_left])
                idx_left += 1
            else:
                result.append(right[idx_right])
                idx_right += 1
        except TypeError as e:
            left_type = type(left[idx_left]).__name__
            right_type = type(right[idx_right]).__name__
            
            raise TypeError(f"Переданы несравнимые экземпляры классов '{right_type}' и '{left_type}'")
            
    result.extend(left[idx_left:])
    result.extend(right[idx_right:])
    return result


def main():
    print("Пример сортировки ...")
    items = [5, 8, 1, 4, -7, 6, 12, 19, -6]
    print(f"Исходный массив: {items}")
    print(f"Отсортированный массив: {merge_sort(items)}")


if __name__ == "__main__":
    main()
