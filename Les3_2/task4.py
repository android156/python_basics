def my_func(x, y):
    pow_x_y = 1
    for i in range(abs(y)):
        pow_x_y /= x
    return pow_x_y

def my_func2(x, y):
    pow_x_y = x ** y
    return pow_x_y

# Добавлены проверки на ввод не правильных значений для float и int, а также через if
# проверка на отрицательность второго параметра
try:
    user_number = float(input('Введите действительное число: '))
    user_pow = int(input('Введите целое отрицательное число: '))
    if user_pow <= 0:
        print(f'{user_number} в степени {user_pow} методом ** {my_func2(user_number, user_pow)} \n'
              f'то же самое через цикл {my_func(user_number, user_pow)}')
    else: print('Второе число должно быть отрицательным!')
except ValueError:
    print('Введено что-то не то. Или набраны буквы или разделитель целой и дробной части отличен от ".",\n'
          'а может второе число не целое')
