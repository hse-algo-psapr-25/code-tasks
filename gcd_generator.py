import random
import main

COMMON_FACTORS = 0
A_ONLY_FACTORS = 1
B_ONLY_FACTORS = 2


class GcdGenerator:
    """Класс для генерации данных для проверки вычисления НОД и НОК.
    Генерация чисел проводится путем возведения простых чисел в случайную
    степень с последующим перемножением полученных множителей. Множители в
    gcd_value содержатся как в a_value, так и в b_value. Другие множители в
    a_value и b_value не пересекаются.

    Properties:
    -----------
    gcd_value -> int:
        Возвращает значение НОД для a_value и b_value.
    a_value -> int:
        Возвращает число, полученное в результате перемножения простых чисел,
        возведенных в случайную степень. Число имеет как общие, так и различные
        множители с числом b_value.
    b_value -> int:
        Возвращает число, полученное в результате перемножения простых чисел,
        возведенных в случайную степень. Число имеет как общие, так и различные
        множители с числом a_value.
    max_factor_cnt -> int:
        Возвращает количество простых множителей, которые можно использовать
        для генерации чисел.
    lcm_value -> int:
        Возвращает значение НОК для a_value и b_value.

    Methods:
    -------
    generate_values(factor_cnt: int = 3, max_pow: int = 5) -> None:
        Процедура генерирует значения a_value, b_value, gcd_value и lcm_value.
        :param factor_cnt: Количество простых чисел, используемых для генерации,
        не должно превышать значение max_factor_cnt. Значение по умолчанию 5.
        :param max_pow: Верхняя граница для случайной степени. Значение по
        умолчанию 5.
        :return: None
    """

    def __init__(self):
        self.__primes: tuple[int] = (
            2,
            3,
            5,
            7,
            11,
            13,
            17,
            19,
            23,
        )
        """Набор простых чисел для генерации значений"""
        self.__values: list[int] = [1, 1, 1]
        """Сгенерированные значения, общие множители (индекс COMMON_FACTORS),
        множители исключительно для a_value (индекс A_ONLY_FACTORS),
        множители исключительно для b_value (индекс B_ONLY_FACTORS)"""
        self.generate_values()

    @property
    def gcd_value(self) -> int:
        """Возвращает значение НОД для a_value и b_value"""
        return self.__values[COMMON_FACTORS]

    @property
    def a_value(self) -> int:
        return self.__values[A_ONLY_FACTORS] * self.__values[COMMON_FACTORS]

    @property
    def b_value(self) -> int:
        return self.__values[B_ONLY_FACTORS] * self.__values[COMMON_FACTORS]

    @property
    def lcm_value(self) -> int:
        return self.a_value * self.b_value // self.gcd_value

    @property
    def max_factor_cnt(self) -> int:
        """Возвращает количество простых множителей, которые можно использовать
        для генерации чисел"""
        return len(self.__primes)

    def generate_values(self, factor_cnt: int = 5, max_pow: int = 5) -> None:
        """Процедура генерирует значения a_value, b_value, gcd_value и lcm_value.
        :param factor_cnt: Количество простых чисел, используемых для генерации,
        не должно превышать значение max_factor_cnt. Значение по умолчанию 5.
        :param max_pow: Верхняя граница для случайной степени. Значение по
        умолчанию 5.
        :return: None
        """
        if factor_cnt > self.max_factor_cnt or factor_cnt < 1:
            raise ValueError("Количество множителей не должно быть больше " + str(self.max_factor_cnt) + " и не меньше 1")
        if max_pow < 1:
            raise ValueError("Степень числа должен быть больше 0")
        
       
        rnd_number = random.sample(self.__primes, factor_cnt)
        
        unikum_a = random.choice(rnd_number)
        rnd_number.remove(unikum_a)
        unikum_b = random.choice(rnd_number)
        rnd_number.remove(unikum_b)

        for k in rnd_number:
            self.__values[COMMON_FACTORS] = self.__values[COMMON_FACTORS] * k ** random.randint(1, max_pow + 1)
        
        self.__values[A_ONLY_FACTORS] = unikum_a ** random.randint(1, max_pow + 1)
        self.__values[B_ONLY_FACTORS] = unikum_b ** random.randint(1, max_pow + 1)
    


if __name__ == "__main__":
    print("Генерация чисел для проверки НОД/НОК")
    generator = GcdGenerator()
    values = generator.generate_values(10, 3)
    print("Число a = %d" % generator.a_value)
    print("Число b = %d" % generator.b_value)
    print("НОД(a, b) = %d" % generator.gcd_value)
    print("НОК(a, b) = %d" % generator.lcm_value)
