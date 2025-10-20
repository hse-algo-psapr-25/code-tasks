from generators.permutation_generator import generate_permutations

"""В данном файле расположен пример использования генератора перестановок.
Генератор, который необходимо реализовать расположен в файле generators/permutation_generator.py"""


def main():
    items = [1, 2, 3]
    print(f"Пример генерации перестановок множества {items}")
    print(generate_permutations(items))


if __name__ == "__main__":
    main()
