
# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running
# (запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в
# режимы: красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами
# должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
# создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.
import time
import itertools
import random


class TrafficLight:
    __color = random.choice(['Красный', 'Жёлтый', 'Зелёный'])  # Начинаем с произвольного

    def running(self):
        time_sleep = [7, 2, 3]
        colors = {'Красный': 0, 'Жёлтый': 1, 'Зелёный': 2}
        self.color = TrafficLight.__color
        print(self.color)
        start_time = time.time()
        end_time = start_time + 20  # Вся фейерия будет происходить 20 секунд
        for i in itertools.count(colors[self.color]):
            print(f'Включен {self.color} на {time_sleep[i % 3]} сек')
            time.sleep(time_sleep[i % 3])
            self.color = list(colors.keys())[(i+1) % 3]
            if time.time() > end_time:
                break
        print('Светофор проработал 20 сек насколько хватило батареек')


tr_1 = TrafficLight()
tr_1.running()
print(f'Что проверять непонятно, порядок зашит в метод')