#  Программа  работает, мультиплеер, много игроков, хоть все компьютерные. Для компьютерных три уровня сложности
#  промахиваются в 10%, 2%, 0%. Логи пишутся в log.txt, время игры для человека считается.

import random
import time
import datetime


# Класс карточек лото. Заполняется при создании экземплярв, как просили, произвольно, без совпадений 5 бочонков
# в каждом ряду на произвольных местах в 3-х 9-тиместных рядах. Все можно поменять в параметрах ниже.
class BarrelList:
    def __init__(self, barrel_quantity=90, row_quantity=3, column_quantity=9, barrel_in_row=5):
        self.barrel_quantity = barrel_quantity
        self.row_quantity = row_quantity
        self.column_quantity = column_quantity
        self.barrel_in_row = barrel_in_row
        self.barrel_set = {el + 1 for el in range(self.barrel_quantity)}
        self.rows_list = []
        self.only_values_list = []
        self.value_places = {}
        for i in range(self.row_quantity):
            random_row_places = random.sample([el for el in range(self.column_quantity)], k=self.barrel_in_row)
            random_row_values = random.sample(list(self.barrel_set), k=self.barrel_in_row)
            self.only_values_list.extend(random_row_values)
            self.barrel_set -= set(random_row_values)
            k = 0
            random_row = []
            for j in range(self.column_quantity):
                if j not in random_row_places:
                    random_row.append('-')
                else:
                    random_row.append(random_row_values[k])
                    self.value_places[random_row_values[k]] = (i, j)
                    k += 1
            self.rows_list.append(random_row)


class Players:
    count_players = 1

    def __init__(self):
        self.name = input(f'Введите имя игрока №{Players.count_players}: ')
        self.is_computer = False
        self.difficulty_level = 0
        self.player_info = {"number": Players.count_players, "name": self.name, "is_computer": self.is_computer,
                            "difficulty_level": self.difficulty_level}
        Game.save_info(f'Создан игрок №{Players.count_players}, {self.name} - человек')
        Players.count_players += 1


class ComputerPlayers(Players):
    count_computer_players = 1
    computer_level_dict = {'1': ['старый калькулятор', 10], '2': ['офисный тормоз', 2], '3': ['киберубийца', 0]}

    def __init__(self):
        self.name = f'cyborg{ComputerPlayers.count_computer_players}'
        self.is_computer = True
        self.difficulty_level = input(f'Введите уровень сложности от 1 до 3: ')
        while not ComputerPlayers.computer_level_dict.get(self.difficulty_level):
            print('Нажмите цифру от 1 до 3: ')
            self.difficulty_level = input()
        self.player_info = {"number": Players.count_players, "name": self.name, "is_computer": self.is_computer,
                            "difficulty_level": ComputerPlayers.computer_level_dict[self.difficulty_level]}
        Game.save_info(f'Создан игрок №{ComputerPlayers.count_players}, {self.name} - компьютер, уровня '
                       f'{ComputerPlayers.computer_level_dict[self.difficulty_level][0]}')
        ComputerPlayers.count_computer_players += 1
        Players.count_players += 1


class Game:  # По умолчанию 2 игрока, но можно хоть 10 из них сколько-то людей, сколько-то компьютеров, кол-во передаем
    # аргументом при создании экземпляра
    turn_count = 0

    def __init__(self, player_quantity=2):
        self.player_quantity = player_quantity
        self.game_parameters = []
        Game.save_info('Началась игра')
        self.start_game_time = time.time()
        who_am_i_dict = {"К": True, "Ч": False, "R": True, "X": False}
        for i in range(self.player_quantity):
            is_computer = who_am_i_dict.get((input(f'Игрок {i + 1} компьютер или человек? '
                                                   f'(нажмите "К" или "Ч"): ')).upper())
            while is_computer is None:
                print('Нажмите "К" или "Ч" раскладка и регистр не имеют значения: ')
                is_computer = who_am_i_dict.get((input()).upper())
            if is_computer:
                player = ComputerPlayers()
            else:
                player = Players()
            barrel_list = BarrelList()
            player.player_info["player_barrel_list"] = barrel_list.rows_list
            player.player_info["only_values_list"] = barrel_list.only_values_list
            player.player_info["value_places"] = barrel_list.value_places
            self.game_parameters.append(player.player_info)
        self.all_barrels_list = {el + 1 for el in range(barrel_list.barrel_quantity)}

    def game_turn(self, parameters, all_barrel_list):
        self.parameters = parameters
        self.all_barrels_list = all_barrel_list
        barrel = random.choice(list(self.all_barrels_list))
        Game.turn_count += 1
        sign_user_loose = []
        print(f'Ход №{Game.turn_count} Из мешка достался бочонок {barrel} Ваш, да или нет? (нажмите "Д" или "Н")')
        yes_or_no_dict = {"Д": True, "Н": False, "L": True, "Y": False}
        self.all_barrels_list -= {barrel}
        for i in range(len(self.parameters)):
            only_values_list = parameters[i]['only_values_list']
            value_places = parameters[i]['value_places']
            human_error = False
            if self.parameters[i]['is_computer']:
                computer_error = True if random.random() * 100 < parameters[i]['difficulty_level'][1] else False
                player_error = computer_error
            else:
                user_yes = yes_or_no_dict.get(input().upper())
                while user_yes is None:
                    print('Нажмите "Д" или "Н" раскладка и регистр не имеют значения: ')
                    user_yes = yes_or_no_dict.get(input().upper())
                if (user_yes and barrel not in only_values_list) or (not user_yes and barrel in only_values_list):
                    human_error = True
                player_error = human_error
            if barrel in only_values_list:
                if not player_error:
                    if self.parameters[i]['is_computer']:
                        print(f'{self.parameters[i]["name"]} ответил Д')
                    self.parameters[i]['only_values_list'].remove(barrel)
                    barrel_row = value_places[barrel][0]
                    barrel_index = value_places[barrel][1]
                    self.parameters[i]['player_barrel_list'][barrel_row].remove(barrel)
                    self.parameters[i]['player_barrel_list'][barrel_row].insert(barrel_index, 'X')
                    if len(only_values_list) == 0:
                        print(f'Игрок №{parameters[i]["number"]} - {parameters[i]["name"]} победил. '
                              f'Все бочонки установлены')
                        Game.save_info(f'Игрок №{parameters[i]["number"]} - {parameters[i]["name"]} победил '
                                       f'на {Game.turn_count} ходу Заполнил все клетки')
                        self.all_barrels_list = []
                        if not self.parameters[i]['is_computer']:
                            end_game_time = time.time()
                            print(f'Показатель по времени {end_game_time-self.start_game_time} сек')
                            Game.save_info(f'Показатель по времени {end_game_time-self.start_game_time} сек')
                        break
                else:
                    if self.parameters[i]['is_computer']:
                        print(f'{self.parameters[i]["name"]} ответил Н')
                    print(f'Игрок №{self.parameters[i]["number"]} - {self.parameters[i]["name"]} проиграл '
                          f'на {Game.turn_count} ходу. Бочонок {barrel} был в карточке!')
                    Game.save_info(f'Игрок №{self.parameters[i]["number"]} - {self.parameters[i]["name"]} проиграл '
                                   f'на {Game.turn_count} ходу. Неправильный ответ')
                    if len(self.parameters) == 1:
                        self.all_barrels_list = []
                    else:
                        sign_user_loose.append(i)
            else:
                if not player_error:
                    if self.parameters[i]['is_computer']:
                        print(f'{self.parameters[i]["name"]} ответил Н')
                else:
                    if self.parameters[i]['is_computer']:
                        print(f'{self.parameters[i]["name"]} ответил Д')
                    print(f'Игрок №{self.parameters[i]["number"]} - {self.parameters[i]["name"]} проиграл '
                          f'на {Game.turn_count} ходу. Бочонок {barrel} в карточке отсутствовал!')
                    Game.save_info(f'Игрок №{self.parameters[i]["number"]} - {self.parameters[i]["name"]} проиграл '
                                   f'на {Game.turn_count} ходу. Неправильный ответ')
                    if len(self.parameters) == 1:
                        self.all_barrels_list = []
                    else:
                        sign_user_loose.append(i)
        sign_user_loose.reverse()
        for i in range(len(sign_user_loose)):
            if len(self.parameters) > 1:
                del self.parameters[sign_user_loose[i]]
            else:
                self.all_barrels_list = []
        return self.parameters, self.all_barrels_list

    def print_barrel_lists(self):  # Иван, спасибо за джойн из задания по матрицам
        for i in range(len(self.game_parameters)):
            barrel_list = '\n'.join([' '.join([str(elem) for elem in line]) for line in
                                     self.game_parameters[i]['player_barrel_list']])
            print(f'карточка игрока №{self.game_parameters[i]["number"]} - {self.game_parameters[i]["name"]} '
                  f'\n{barrel_list}')

    @staticmethod  # Из-за статикметода тут нет селфа, вызвать можно Game.save_info()
    def save_info(message=''):
        current_time = datetime.datetime.now()
        result = f'{current_time} - {message}'
        with open('log.txt', 'a', encoding='utf-8') as f:
            f.write(result + '\n')


a = Game(3)  #  Запуск для троих игоков
a.print_barrel_lists()
game_parameters = a.game_parameters
all_barrel_list = a.all_barrels_list
while a.all_barrels_list:
    game_parameters, all_barrel_list = a.game_turn(a.game_parameters, a.all_barrels_list)
    a.print_barrel_lists()
