
# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула(куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Выполните
# вызов методов и также покажите результат.

# Получил удовольствие, разобрался. Чутка усложнил, добавил логики, все вроде работает, допер зачем и как работает
# super. Show speed у всех переопределено. Базовый остался только у GolfCar

import random


class Car:
    def __init__(self, color, name, speed=0, is_police=False, direction=None):
        print(f'Создан экземпляр производного класса {self.__class__.__name__} '
              f'от базового класса {__class__.__name__}')
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.direction = direction

    def go(self):
        if not self.speed:
            self.speed = random.randint(1, 101)  # стартуем с произвольной скоростью в произвольном направлении
            self.direction = random.choice(["на север", "на юг", "в неизвестном направлении", "на запад", "направо",
                                            "вдаль", "в рай", "в направлении заката"])
            print(f'Объект {self.__class__.__name__} {self.name} поехал')
        else:
            print(f'Объект {self.__class__.__name__} {self.name} уже в движении')

    def stop(self):
        self.speed = 0
        print('Машина остановилась')

    def turn(self, direction):
        if self.speed:
            self.direction = direction
            print(f'Машина повернула {direction}')
        else:
            self.go()
            self.direction = direction

    def show_speed(self):
        print(f'Скорость машины {self.__class__.__name__} -  {self.speed} км/ч')

    def get_full_info(self):  # Можно считать, что в этом методе все атрибуты опробованы
        car_type = 'полицейская' if self.is_police else 'гражданская'
        car_condition = f'едет со скоростью {self.speed} км/ч {self.direction}' if self.speed else 'стоит на месте'
        print(f'Имя {self.__class__.__name__} {self.name}, цвет - {self.color}, {car_type}, {car_condition}')


class TownCar(Car):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        super().__init__(color, name)

    def show_speed(self):
        if self.speed:
            print(f'Скорость машины {self.speed} км/ч. Двигается с разрешенной скоростью.'
                  if self.speed <= 40
                  else f'Скорость машины {self.speed} км/ч. ПРЕВЫШЕНИЕ!!!')
        else:
            print("Стоит на месте. Скорость 0.")


class SportCar(Car):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        super().__init__(color, name)

    def go(self):
        if not self.speed:
            self.speed = random.randint(100, 301)  # стартуем с произвольной мегаскоростью в произвольном направлении
            # это ж спорткар, Карл! Полетели!
            self.direction = random.choice(["на север", "на юг", "в неизвестном направлении", "на запад", "направо",
                                            "вдаль", "в рай", "в направлении заката"])
            print(f'Объект {self.__class__.__name__} {self.name} полетел')
        else:
            print(f'Объект {self.__class__.__name__} {self.name} уже в стремительном движении.')

    def show_speed(self):
        if self.speed:
            print(f'Скорость машины {self.speed} км/ч. На таком космолете, так можно.'
                  if self.speed <= 200
                  else f'Скорость машины {self.speed} км/ч. Внимание, смертник!!!')
        else:
            print("Стоит на месте. Скорость 0.")


class WorkCar(Car):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        super().__init__(color, name)

    def show_speed(self):
        if self.speed:
            print(f'Скорость машины {self.speed} км/ч. Разрешенная скорость'
                  if self.speed <= 40
                  else f'Скорость машины {self.speed} км/ч. ПРЕВЫШЕНИЕ!!!')
        else:
            print("Стоит на месте. Скорость 0.")


class PoliceCar(Car):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        super().__init__(color, name, is_police=True)

    def show_speed(self):
        print(f'Скорость машины -  {self.speed} км/ч. Полиции все можно. Еще бы мигалку включали')


class GolfCar(Car):
    def __init__(self, color, name):
        self.color = color
        self.name = name
        super().__init__(color, name)


police_car = PoliceCar('Black/white', '156')
police_car.get_full_info()
police_car.turn('Налево')
police_car.go()
police_car.get_full_info()
police_car.show_speed()
work_car = WorkCar("Красный", "Пикап")
work_car.get_full_info()
work_car.go()
work_car.get_full_info()
work_car.show_speed()
sport_car = SportCar("Желтый", "Ламбоджини Диабло")
sport_car.go()
sport_car.show_speed()
town_car = TownCar("Баклажан", "Заниженная Приора")
town_car.go()
town_car.get_full_info()
town_car.turn('в сторону Эльорадо')
town_car.get_full_info()
town_car.stop()
town_car.get_full_info()
town_car.show_speed()
town_car.go()
town_car.show_speed()
town_car.go()
town_car.get_full_info()
golf_car = GolfCar('Голубой', "Тарантас")
golf_car.go()
golf_car.show_speed()
