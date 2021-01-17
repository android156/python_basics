#  Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname,
#  position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться
#  на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
#  Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы
#  получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
#  Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
#  проверить значения атрибутов, вызвать методы экземпляров).

class Worker:
    count = 0

    def __init__(self, name, surname):
        Worker.count += 1
        print(f'Представитель №{Worker.count} класса {self.__class__.__name__} подкласса {__class__.__name__} создан')
        self.name = name
        self.surname = surname
        # Остальные атрибуты в Position, но на всякий случай прикладываю решение со всеми 4мя в этом месте, словарь
        # применял свой, более приближенный к реальности. Однострочный из условия странный, никто так хранить не будет.


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname)
        self.position = position
        self._income = sum(income[position])
        print(f'Должность {self.position} класса {self.__class__.__name__} создана')

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return f'{self._income}'


secret_dict1 = {"wage": 250000, "bonus": 50000}
# В идеале словарь с должностями иметь со всеми деньгами и бонусами к каждой должности
# Пожалуй так и сделаю. Допускаю, что к каждому сотруднику можно и персонально платить,
# не зависимо от должности, но исправить будет не сложно, если что.

# код под нормальный человеческий словарь
secret_dict2 = {'Директор по продажам': [250000, 50000],
                'Главный менеджер': [170000, 30000],
                'Старший менеджер': [150000, 25000],
                'Менеджер': [120000, 15000],
                'Уборщица': [30000, 15000]}
worker1 = Position('Николай', 'Дегтярев', 'Директор по продажам', secret_dict2)
print(f'Получено полное имя: {worker1.get_full_name()}')
print(f'Получен полный доход: {worker1.get_total_income()}')
worker2 = Position('Иван', 'Петров', 'Старший менеджер', secret_dict2)
print(f'Получено полное имя: {worker2.get_full_name()}')
print(f'Получен полный доход: {worker2.get_total_income()}')
worker3 = Position('Андрей', 'Сидоров', 'Менеджер', secret_dict2)
print(f'Получено полное имя: {worker3.get_full_name()}')
print(f'Получен полный доход: {worker3.get_total_income()}')
