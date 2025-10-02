from data_structures.lists.base_list import BaseList
from data_structures.lists.doubly_linked_list.doubly_list_node import DoublyListNode


class DoublyLinkedList(BaseList):
    """
    Реализация двусвязного списка.

    Атрибуты:
        head (DoublyListNode | None): ссылка на первый элемент списка.
        tail (DoublyListNode | None): ссылка на последний элемент списка.
        size (int): количество элементов в списке.

    Поддерживаемые операции:
        - append(value): добавить элемент в конец
        - appendleft(value): добавить элемент в начало
        - insert(index, value): вставить элемент по индексу
        - remove(value): удалить первый найденный элемент
        - pop(): удалить последний элемент и вернуть его
        - popleft(): удалить первый элемент и вернуть его
        - index(value): вернуть индекс первого найденного элемента
        - __str__(): вернуть строковое представление двусвязного списка
        - __len__(): вернуть количество элементов
        - __iter__(): прямой обход
        - __reversed__(): обратный обход
    """

    def __init__(self):
        """Создаёт пустой двусвязный список."""
        self.head = None
        self.tail = None
        self.size = 0



    # ==== служебные методы ====
    def _check_index_for_insert(self, index: int):
        """Проверяет корректность индекса для вставки (0 ≤ index ≤ size)."""
        if not isinstance(index, int):
            raise TypeError("Индекс должен быть целым числом")
        if index < 0 or index > self.size:
            raise IndexError("Индекс вне допустимого диапазона")

    def _node_at(self, index: int) -> DoublyListNode:
        """Возвращает узел по индексу (0 ≤ index < size)."""
        if index < 0 or index >= self.size:
            raise IndexError("Индекс вне допустимого диапазона")

        # Оптимизируем направление прохода: с головы или с хвоста
        if index <= self.size // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            return cur
        else:
            cur = self.tail
            for _ in range(self.size - 1, index, -1):
                cur = cur.prev
            return cur



    def append(self, value):
        """Добавляет элемент в конец списка. O(1)."""
        new_node = DoublyListNode(value)
        if self.tail is None:                  # пустой список
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node          # старый хвост → новый
            new_node.prev = self.tail          # новый знает старый хвост
            self.tail = new_node               # сдвигаем хвост
        self.size += 1

    def appendleft(self, value):
        """Добавляет элемент в начало списка. O(1)."""
        new_node = DoublyListNode(value)
        if self.head is None:                  # пустой список
            self.head = self.tail = new_node
        else:
            new_node.next = self.head          # новый указывает на старую голову
            self.head.prev = new_node          # старая голова знает нового слева
            self.head = new_node               # сдвигаем голову
        self.size += 1


    def insert(self, index, value):
        """Вставляет элемент по указанному индексу (0 ≤ index ≤ len)."""
        self._check_index_for_insert(index)
        if index == self.size:
            # Вставка в конец эквивалентна append
            self.append(value)
            return
        if index == 0:
            # Вставка в начало эквивалентна appendleft
            self.appendleft(value)
            return

        next_node = self._node_at(index)
        prev_node = next_node.prev
        node = DoublyListNode(value)

        # Связываем prev <-> node <-> next
        node.prev = prev_node
        node.next = next_node
        if prev_node:
            prev_node.next = node
        next_node.prev = node

        self.size += 1

    def remove(self, value):
        """Удаляет первое вхождение value. Если не найдено — ValueError. O(n)."""
        cur = self.head
        while cur is not None:
            if cur.value == value:
                prev_node, next_node = cur.prev, cur.next

                if prev_node is None:
                    self.head = next_node
                else:
                    prev_node.next = next_node

                if next_node is None:
                    self.tail = prev_node
                else:
                    next_node.prev = prev_node

                cur.prev = cur.next = None
                self.size -= 1
                return
            cur = cur.next
        raise ValueError("value not in list")


    def pop(self):
        """Удаляет и возвращает последний элемент. Пусто -> IndexError. O(1)."""
        if self.tail is None:
            raise IndexError("pop from empty list")
        node = self.tail
        prev_node = node.prev

        if prev_node is None:                    # единственный элемент
            self.head = self.tail = None
        else:
            prev_node.next = None
            self.tail = prev_node

        node.prev = node.next = None
        self.size -= 1
        return node.value


    def popleft(self):
        """Удаляет и возвращает первый элемент. Пусто -> IndexError. O(1)."""
        if self.head is None:
            raise IndexError("popleft from empty list")
        node = self.head
        next_node = node.next

        if next_node is None:                    # единственный элемент
            self.head = self.tail = None
        else:
            next_node.prev = None
            self.head = next_node

        node.prev = node.next = None
        self.size -= 1
        return node.value


    def index(self, value):
        """Возвращает индекс первого узла с данным значением или None, если не найдено."""
        i = 0
        cur = self.head
        while cur:
            if cur.value == value:
                return i
            i += 1
            cur = cur.next
        return None

    def __str__(self) -> str:
        """Возвращает строковое представление двусвязного списка."""
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " <-> ".join(values)

    def __len__(self):
        """Возвращает количество элементов в списке."""
        return self.size

    def __iter__(self):
        """Итерирует по значениям слева направо."""
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def __reversed__(self):
        """Итерирует по значениям справа налево."""
        cur = self.tail
        while cur:
            yield cur.value
            cur = cur.prev

if __name__ == "__main__":
    dll = DoublyLinkedList()

    dll.append(10)
    dll.append(20)
    dll.append(30)
    print("После добавления:", dll)

    dll.insert(0, 5)
    print("После вставки в начало:", dll)

    dll.insert(2, 15)
    print("После вставки в середину:", dll)

    dll.remove(20)
    print("После удаления 20:", dll)

    idx = dll.index(30)
    print(f"Индекс элемента 30: {idx}")

    print("Размер списка:", len(dll))

    print("Элементы списка:", [x for x in dll])

    print("Обратный обход:", [x for x in reversed(dll)])