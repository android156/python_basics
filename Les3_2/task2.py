# Выполнить функцию, которая принимает несколько параметров, описывающих данные
# пользователя: имя, фамилия, год рождения, город проживания, email, телефон. Функция
# должна принимать параметры как именованные аргументы. Осуществить вывод данных о
# пользователе одной строкой.
def print_all_about_user(userinfo):
    list = []
    for key in userinfo.keys():
        print(userinfo[key], end=' ') #Возвращаем все в строку
        list.append(userinfo[key])
    print(' ')
    print(list) # Возращаем строкой
    print(userinfo.values()) # Возвращаем значениями словаря тоже вроде в строку

#Вот тут снова возникает вопрос, где переменные должны называться точнее или красивее
# в функции, где они описаны или в теле программы, от которых мы функцию запускаем?
# Нужно ли вводить новые переменные или названия можно задублировать? Я задублировал,
# (userinfo как в теле программы, так и аргумент функции) но не уверен, что это хорошо,
# хотя, тут работает, буду рад замечаниям.
userinfo = {
    'Имя': 'Василий',
    'Фамилия': 'Пупкин',
    'Год рождения': '2000',
    'Город проживания': 'Чернобыль',
    'Email': 'pupkin@yandex.ru',
    'Телефон': '+7(001)001-01-01'
    }
print_all_about_user(userinfo)


