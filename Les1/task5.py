print('Программа "Милый ваш бухгалтер" приветствует Вас!')
income = int(input('Введите выручку нашей конторы в рублях: '))
charges = int(input('Введите расходы нашей конторы в рублях: '))
profit = income - charges
if income > charges:
    print(f'Мы прибыльная организация. Наша прибыль {profit} рублей')
    print(f'Наша рентабельность {int(profit/income*100) // 1}% (округлено до целого)')
    number_staff = int(input('Сколько у нас сотрудников: '))
    print(f'прибыль в пересчете на каждого сотрудника {int(profit/number_staff)} (округлено до целого)')
else:
    print(f'Мы убыточная организация. Наш убыток {-profit} рублей')