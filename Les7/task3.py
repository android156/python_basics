# 3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. В его конструкторе
# инициализировать параметр, соответствующий количеству клеток (целое число). В классе должны быть реализованы методы
# перегрузки арифметических операторов: сложение (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
# (__truediv__()).Данные методы должны применяться только к клеткам и выполнять увеличение, уменьшение, умножение и
# обычное (не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться округление значения
# до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки должно равняться сумме ячеек исходных двух
# клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только если разность количества ячеек двух клеток
# больше нуля, иначе выводить соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки определяется как произведение количества ячеек
# этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки определяется как целочисленное деление количества
# ячеек этих двух клеток.
# В классе необходимо реализовать метод make_order(), принимающий экземпляр класса и количество ячеек в ряду. Данный
# метод позволяет организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где количество ячеек между \n равно переданному аргументу.
# Если ячеек на формирование ряда не хватает, то в последний ряд записываются все оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в ряду — 5. Тогда метод make_order() вернет строку:
# *****\n*****\n**. Если количество ячеек клетки равняется 15, количество ячеек в ряду — 5. Тогда метод make_order()
# вернет строку: *****\n*****\n*****.
import random


class Cells:
    def __init__(self):
        self.number_cell_parts = random.randint(1, 21)
        print(f'Создана клетка, в ней {self.number_cell_parts} ячеек')

    def __add__(self, other):
        print(f'Складываем клетку размером {self.number_cell_parts} и {other.number_cell_parts} ячеек')
        self.number_cell_parts += other.number_cell_parts
        del other
        return self

    def __mul__(self, other):
        print(f'Умножаем клетку размером {self.number_cell_parts} ячеек на клетку {other.number_cell_parts} ячеек')
        self.number_cell_parts *= other.number_cell_parts
        del other
        return self

    def __sub__(self, other):
        print(f'Вычитаем из клетки с {self.number_cell_parts} ячейками, клетку с {other.number_cell_parts} ячейками')
        if self.number_cell_parts > other.number_cell_parts:
            self.number_cell_parts -= other.number_cell_parts
            del other
            return self
        else:
            print('Это не возможно, вычитаемая клетка больше')

    #   про деление условие традиционно сформулировано, так, что черт ногу сломит. Сверху написано про округление,
    #   при расшифровке деления ниже взято целочисленное деление. Использовал целочисленное, надеюсь, что поверите,
    #   что я умею делить не только на цело, но и пользоваться round
    def __truediv__(self, other):
        print(f'Делим клетку размером {self.number_cell_parts} ячеек на клетку {other.number_cell_parts} ячеек')
        if self.number_cell_parts > other.number_cell_parts:
            self.number_cell_parts = self.number_cell_parts//other.number_cell_parts
            del other
            return self
        else:
            print('Это не возможно, клетка-делитель больше')

    def make_order(self, quantity_in_row):
        result_str = ''
        row_quantity = self.number_cell_parts // quantity_in_row
        for j in range(row_quantity):
            result_str += '*'*quantity_in_row+'\n'
        result_str += '*'*(self.number_cell_parts % quantity_in_row)+'\n'
        print(f'Клетка размером {self.number_cell_parts}, рядами по {quantity_in_row} :\n{result_str}')


# Все методы работают.
a = Cells()
b = Cells()
a.make_order(5)
b.make_order(3)
c = a*b
c.make_order(10)
d = Cells()
e = Cells()
g = d-e if d.number_cell_parts > e.number_cell_parts else e-d
g.make_order(10)
c = a+g
c.make_order(10)
e = c/g
e.make_order(3)
