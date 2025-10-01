from data_structures.linked_list.list_node import ListNode


class LinkedList:
    """
    Класс, реализующий односвязный список.

    Атрибуты:
        head (Node | None): ссылка на первый узел списка.
        size (int): количество элементов в списке.

    Поддерживает базовые операции:
        - добавление элемента в конец (append),
        - вставка по индексу (insert),
        - удаление элемента по значению (remove),
        - поиск индекса элемента (index),
        - получение длины (__len__),
        - итерация (__iter__),
        - строковое представление (__str__).
    """

    def __init__(self):
        """Создаёт пустой связный список."""
        self.head = None
        self.size = 0

    def append(self, value):
        """
        Добавляет элемент в конец списка.

        Аргументы:
            value: значение нового элемента.
        """
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
        self.size += 1

    def insert(self, index, value):
        """
        Вставляет элемент по указанному индексу.

        Аргументы:
            index (int): позиция вставки (0 ≤ index ≤ len).
            value: значение нового элемента.

        Исключения:
            IndexError — если индекс вне диапазона.
        """
        if index < 0 or index > self.size:
            raise IndexError("Index out of range.")

        new_node = ListNode(value)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            if self.head is None:
                raise IndexError("Index out of range.")
            current = self.head
            for _ in range(index - 1):
                if current.next is None:
                    raise IndexError("Index out of range.")
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def remove(self, value):
        """
        Удаляет первый элемент с указанным значением.

        Аргументы:
            value: значение для удаления.

        Исключения:
            ValueError — если элемента с таким значением нет.
        """
        if self.head is None:
            raise ValueError(f"Element with value {value} not found.")
        if self.head.value == value:
            self.head = self.head.next
            self.size -= 1
            return
        else:
            current = self.head
            while current.next is not None:
                if current.next.value == value:
                    current.next = current.next.next
                    self.size -= 1
                    return
                current = current.next
            raise ValueError(f"Element with value {value} not found.")

    def index(self, value):
        """
        Возвращает индекс первого элемента с указанным значением.

        Аргументы:
            value: искомое значение.

        Возвращает:
            int: индекс элемента, если найден.
            None: если элемент отсутствует.
        """
        current = self.head
        idx = 0
        while current is not None:
            if current.value == value:
                return idx
            current = current.next
            idx += 1
        return None

    def __len__(self):
        """Возвращает количество элементов в списке."""
        return self.size

    def __iter__(self):
        """
        Позволяет итерироваться по элементам списка в цикле for.

        Использование:
            for x in my_list:
                ...

        """
        current = self.head
        while current is not None:
            yield current.value
            current = current.next

    def __str__(self):
        """
        Возвращает строковое представление списка.

        Формат:
            [elem1 -> elem2 -> elem3]

        Использование:
            print(my_list)
        """
        values = [str(v) for v in self]
        return "[" + " -> ".join(values) + "]"


if __name__ == "__main__":
    lst = LinkedList()
    print("Создан пустой список:", lst)

    lst.append(10)
    lst.append(20)
    lst.append(30)
    print("После добавления элементов:", lst)

    lst.insert(1, 15)
    print("После вставки 15 в позицию 1:", lst)

    lst.remove(20)
    print("После удаления элемента 20:", lst)

    idx = lst.index(30)
    print("Индекс элемента 30:", idx)
    print("Поиск отсутствующего элемента:", lst.index(99))

    print("Элементы в списке через цикл for:")
    for x in lst:
        print(x)

    print("Длина списка:", len(lst))
