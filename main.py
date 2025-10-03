from data_structures.lists.doubly_linked_list.doubly_linked_list import DoublyLinkedList
from data_structures.lists.linked_list.linked_list import LinkedList


def main():
    print("Использование односвязного списка")
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

    print("Использование двусвязного списка")
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


if __name__ == "__main__":
    main()
