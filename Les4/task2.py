# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Подсказка: элементы,
# удовлетворяющие условию, оформить в виде списка. Для формирования списка
# использовать генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

from random import randint
number_list = []
for i in range(20):
    number_list.append(randint(0, 10))
print(number_list)
# критический момент при выборе из списка первого элемента с индексом 0
# тогда сравнение идет с последним элементом, но это мы учли добавив условие,
# что элемент с индексом 0 берем всегда. Также не понятно, что делать если
# есть повторные элементы и индекс выдаст место первого такого элемента, к примеру
# если первое число дальше встречается много раз, а оно априори берется и метод
# index будет всегда брать его с 0 места и пихать в результат, хотя не следует
# new_number_list = [x for i,x in number_list if number_list.index(x) == 0
#                              or x > number_list[number_list.index(x)-1]]
# А вот если номер элемента брать через enumerate, то мы все это устраним
new_number_list = [x for i,x in enumerate(number_list) if i == 0 or x > number_list[i-1]]
print(new_number_list)