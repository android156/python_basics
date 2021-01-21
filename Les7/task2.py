# Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное
# название. К типам одежды в этом проекте относятся пальто и костюм. У этих типов
# одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут
# быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для
# пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3). Проверить работу этих методов
# на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на
# этом уроке знания: реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

import abc

# Выдает ошибку при отсутствии соответствующих методов классе Clothes и предупреждение
# при не совпадении кол-ва аргументов видимо смысл этого класса в этом.


class MyAbsClass(abc.ABC):
    @abc.abstractmethod
    def coat_cloth_volume(self, v):
        pass

    @abc.abstractmethod
    def suit_cloth_volume(self, h):
        pass


# Класс один Clothes по типу абстрактного. В идеале для костюмов и пальто завести отдельные классы,
# но в условии написано было про обин класс. Исходя из материалов вебинара усвоено, что за тех. задание
# выходить не стоит, заказчик не поймет))
class Clothes(MyAbsClass):
    clothes_list = []

    def __init__(self, name, cl_type, size_or_high):
        self.name = name
        self._cl_type = cl_type
        self.size_or_high = size_or_high
        if self.cl_type == 'пальто':
            self.cloth_volume = Clothes.coat_cloth_volume(self, self.size_or_high)
        elif self.cl_type == 'костюм':
            self.cloth_volume = Clothes.suit_cloth_volume(self, self.size_or_high)
        else:
            self.cloth_volume = 0
            print(f'{cl_type} - Неизвестный тип одежды, в расчете ткани учитываться не будет')
        Clothes.clothes_list.append([self.name, self.cl_type, self.size_or_high, round(self.cloth_volume, 1)])
        print(f'Создан объект {self.name} экземпляр класса {self.__class__.__name__}, тип {self.cl_type}')

# Декоратор работает заменяя, все неизвестное типом неизвестный
    @property
    def cl_type(self):
        if self._cl_type not in ['пальто', 'костюм']:
            self._cl_type = 'неизвестный'
        return self._cl_type

# реплики необходимых методы прописанные в абстрактном классе
    def coat_cloth_volume(self, v):
        return v/6.5 + 0.5

    def suit_cloth_volume(self, h):
        return 2 * h + 0.3

# Самый главный расчет
def common_volume():
    cloth_volume = sum([x[3] for x in Clothes.clothes_list])
    return round(cloth_volume, 1)


# Все считается верно, логику в подсчетах понять не удалось
a = Clothes('плащ палатка', 'пальто', 54)
b = Clothes('наряд короля', 'костюм', 1.8)
c = Clothes('розовое пальто', 'пальто', 44)
d = Clothes('Попона', 'накидка', 44)

print(f'Вся база одежды \n{Clothes.clothes_list}')
print(f' Общая потребность ткани {common_volume()}')
