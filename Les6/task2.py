# Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать
# защищенными. Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного
# полотна. Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги
# асфальтом, толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т

class Road:
    def __init__(self, length, width):
        print(f'Экземпляр {self.__class__.__name__} создан')
        self._length = length
        self._width = width
        print(f'Значения защищенных атрибутов length = {self._length}, width = {self._width}')

    def calculate(self, weight, thickness):
        # Вторая функция необязательна, можно было все в init запихать,
        # но просили вроде только 2 параметра при создании класса передавать
        self.weight = weight
        self.thickness = thickness
        return self._length*self._width*self.weight*self.thickness


# Длина, ширина в метрах, толщина в см, вес в кг
length = 20000
width = 6
thickness = 10
weight = 50
road_to_hell = Road(length, width)
print(f'Толщина покрытия {thickness} см, вес 1 квадратного метра толщиной 1см - {weight} кг')
road_to_hell.calculate(weight, thickness)
print(f'Асфальту понадобится {round(road_to_hell.calculate(weight, thickness)/1000, 2)} тонн')
