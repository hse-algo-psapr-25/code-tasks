from schedules.schedule import Schedule
from schedules.task import Task


if __name__ == "__main__":
    print("Пример использования класса Schedule")

    # Инициализируем входные данные для составления расписания
    tasks = [
        Task("a", 3),
        Task("b", 4),
        Task("c", 6),
        Task("d", 7),
        Task("e", 7),
        Task("f", 9),
        Task("g", 10),
        Task("h", 12),
        Task("i", 17),
    ]

    # Инициализируем экземпляр класса Schedule
    # при этом будет рассчитано расписание для каждого исполнителя
    schedule = Schedule(tasks, 5)

    # Выведем в консоль полученное расписание
    print(schedule)
    for i in range(schedule.executor_count):
        print(f"\nРасписание для исполнителя # {i + 1}:")
        for schedule_item in schedule.get_schedule_for_executor(i):
            print(schedule_item)
