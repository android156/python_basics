# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21.
# Необходимо решить задание в одну строку.
# Подсказка: использовать функцию range() и генератор.

from random import randint
number_list = []
for i in range(50):
    number_list.append(randint(20, 240))
print(number_list)
new_number_list = [x for x in number_list if x % 20 == 0 or x % 21 == 0]
print(new_number_list)

# Надо же еще все повыводить, да список создать, в одну строку никак)))