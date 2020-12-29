def divide(divisible, divisor):
    """
    # Test description
    :param divisible: It's divisible
    :param divisor: It's divisor
    :return: It's result divisible/divisor
    """
    try:
        return divisible / divisor
    except ZeroDivisionError:
        print('Деление на ноль!')
    except ValueError:
        print('Введено не число!')


#Вот тут возникает вопрос, где переменные должны называться точнее в функции,
# где они описаны или те от которых мы функцию запускаем? Нужно ли вводить
# новые переменные или названия можно задублировать? Я задублировал,
# но не уверен, что это хорошо, буду рад замечаниям.
# добавлено 2 проверки на делимое и делитель, что это числа.
try:
    divisible = float(input( "Укажите делимое: "))
    try:
        divisor = float(input("Укажите делитель: "))
        print(f'{divisible}/{divisor} = {round(divide(divisible, divisor), 2)} '
              f'(результат округлен до сотых долей)')
    except ValueError:
        print('Введено не число!')
except ValueError:
    print('Введено не число!')
