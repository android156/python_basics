# Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию. Элементы
# вывести в порядке их следования в исходном списке. Для выполнения задания
# обязательно использовать генератор.

# Напрашивается решение прогнать список через set) Но генератор, так генератор

from random import randint
number_list = []
for i in range(20):
    number_list.append(randint(1, 20))
print(number_list)
new_number_list = [x for x in number_list if number_list.count(x) == 1]
print(new_number_list)
