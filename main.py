from collections import namedtuple

from strenum import StrEnum

SomeResult = namedtuple("SomeResult", ["first_field", "second_field"])


class ErrorMessages(StrEnum):
    """Перечисление сообщений об ошибках."""

    SOME_ERROR = "Что-то пошло не так..."
    OTHER_ERROR = "Ошибка ..."


def some_function(some_parameter: int, other_parameter) -> SomeResult:
    """Описание функции, параметров, исключений и возвращаемого результата"""
    ...


def main():
    """Примеры использования разрабатываемой функции"""
    ...


if __name__ == "__main__":
    main()
