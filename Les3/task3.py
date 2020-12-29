# Реализовать функцию my_func(), которая принимает три позиционных аргумента и
# возвращает сумму наибольших двух аргументов.

# Нормально ли назвать в данной фунуции аргументы буквами a, b, c или, как и в
# теле программы указывать number1, number2 и number3? Или если в функции все
# расшифровать, то все культурно? Или взять, как и в предыдущих заданиях
# переменные из тела программы?
def my_func(a, b, c):
    """
    :param a: число 1
    :param b: число 2
    :param c: число 3
    :return: Сумма максимумов двух аргументов
    """
    user_numbers = []
    user_numbers.append(a)
    user_numbers.append(b)
    user_numbers.append(c)
    return sum(user_numbers) - min(user_numbers)


user_number1 = float(input('Введите число 1: '))
user_number2 = float(input('Введите число 2: '))
user_number3 = float(input('Введите число 3: '))
print(f'Сумма наибольших двух аргументов {my_func(user_number1, user_number2, user_number3)}')
