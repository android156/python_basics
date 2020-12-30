# Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
# Подсказка: использовать функцию count() и cycle() модуля itertools. Обратите
# внимание, что создаваемый цикл не должен быть бесконечным. Необходимо
# предусмотреть условие его завершения.
#

from itertools import count, cycle
from random import randint
from time import time, sleep

start = int(input('Введите первое число: '))
for i in count(start):
    print(i)
    if i == 20:  # Числа до 20 от введенного
        break

number_list = []
for i in range(7):
    number_list.append(randint(1, 10))
print(number_list)
sleep(2)
start_time = time()
end_time = start_time + 0.0005  # Ограничение по времени.
# Будем выводить элементы списка 0,0005 сек
for i in cycle(number_list):
    print(i, end=' ')
    if time() > end_time:
        break
