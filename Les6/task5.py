#  Реализовать класс Stationery (канцелярская принадлежность). Определить в нем атрибут title (название) и метод
#  draw (отрисовка). Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen (ручка), Pencil
#  (карандаш), Handle (маркер). В каждом из классов реализовать переопределение метода draw. Для каждого из классов
#  методы должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод
#  для каждого экземпляра.

class Stationery:
    def __init__(self):
        self.title = self.__class__.__name__  # непонятно зачем нужен этот атрибут, но раз просят на здоровье!
        print(f'Создан экземпляр класса {self.title} подкласса {__class__.__name__}' if self.title != __class__.__name__
              else f'Создан экземпляр класса {self.title}')

    def draw(self):
        print(f'Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Отрисовка инструментом Pen тонкая линия цвета разные')


class Pencil(Stationery):
    def draw(self):
        print('Отрисовка инструментом Pencil - тонкая серая линия')


class Handle(Stationery):
    def __init__(self):
        super().__init__()

    def draw(self):
        print('Отрисовка инструментом Handle - жирная линия')


unknown_tool = Stationery()
unknown_tool.draw()
pen = Pen()
pencil = Pencil()
handle = Handle()
pen.draw()
pencil.draw()
handle.draw()
