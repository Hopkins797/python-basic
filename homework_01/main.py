"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [number ** 2 for number in numbers]

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):

    result = number != 1
    for n in range(2, number//2+1):
        if number % n == 0:
            result = False
            break
    return result

def filter_numbers(number_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >> filter_numbers([1, 2, 3], ODD)
    << [1, 3]
    >> filter_numbers([2, 3, 4, 5], EVEN)
    << [2, 4]
    """
    if filter_type == ODD:
        return [number for number in number_list if number % 2 != 0]
    if filter_type == EVEN:
        return [number for number in number_list if number % 2 == 0]
    if filter_type == PRIME:
        return [number for number in number_list if is_prime(number)==True]


# print(filter_numbers([1,2,3,5,6,7,8,9,10,11,12,13,14,15,17,18, 19,20, 23, 29], PRIME))
# print(power_numbers(1,2,3,4))
