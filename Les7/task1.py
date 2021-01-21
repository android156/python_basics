# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод __init__()), который должен принимать данные (список списков)
# для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных
# в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в
# привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения
# двух объектов класса Matrix (двух матриц). Результатом сложения должна быть
# новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент
# первой строки первой матрицы складываем с первым элементом первой строки
# второй матрицы и т.д.


import random


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        result_for_print = ''
        for el in self.matrix_list:
            result_str = ''
            for number in el:
                result_str += f'{number}  '
            result_for_print += f'{result_str}\n'
        return result_for_print

# Сравнение матриц также через перехват решил сделать
    def __eq__(self, other):
        eq_result = True
        if len(self.matrix_list) == len(other.matrix_list):
            for i in range(len(self.matrix_list)):
                if len(self.matrix_list[i]) != len(other.matrix_list[i]):
                    eq_result = False
                    break
        else:
            eq_result = False
        return eq_result

    def __add__(self, other):
        # Чтобы выдать в результате объект  и не испортить входящие
        # создаем новый внутри метода (композиция???) Можно было бы
        # выдавать список-результат, но тогда принт не будет перехватываться
        # для суммы)
        sum_result = Matrix([])
        for self_el, other_el in zip(self.matrix_list, other.matrix_list):
            sum_el = [x + y for x, y in zip(self_el, other_el)]
            sum_result.matrix_list.append(sum_el)
        return sum_result


# Получаем матрицу width * high заполненную  произвольными целыми числами
# от -100 до 100, в идеале это сразу сделать в ините класса, но строго наказано
# передавать туда список, поэтому это здесь
def get_matrix(matrix_width, matrix_high):
    matrix = []
    matrix_str = []
    for i in range(matrix_high):
        matrix.append(matrix_str.copy())
        for j in range(matrix_width):
            matrix[i].append(random.randint(-100, 101))
    return matrix


a = Matrix(get_matrix(2, 2))
b = Matrix(get_matrix(2, 2))
c = Matrix(get_matrix(6, 3))

print(a)
print(b)
print(c)

print(f' Матрицы одинаковых размеров. Результат сложения \n'
      f' {a + b}' if a == b else f'Матрицы разных размеров, сложение невозможно')

print(f' Матрицы одинаковых размеров. Результат сложения \n'
      f' {a + c}' if a == c else f'Матрицы разных размеров, сложение невозможно')
