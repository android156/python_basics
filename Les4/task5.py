# Реализовать формирование списка, используя функцию range() и возможности
# генератора. В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.

from functools import reduce
number_list = []
number_list = list(range(100, 1000, 2))
print(number_list)
print(reduce(lambda x, y: x * y, number_list))
