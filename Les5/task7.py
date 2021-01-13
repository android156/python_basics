import json

res_list = []
res_dict = {}
average_dict = {}
income = 0
average_income = 0
income_list = []
count = 0
#  Задачу чутка усложнил, названия фирм могут состоять из нескольких слов
with open('companies.txt', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())
        list_line = line.split()
        income = int(list_line[-2])-int(list_line[-1])
        res_dict[' '.join(list_line[:len(list_line)-3])] = income
        if income > 0:
            average_income += income
            count += 1
average_dict['Cредняя прибыль'] = 'Все убыточные' if count == 0 else round(average_income/count)
res_list.append(res_dict)
res_list.append(average_dict)
print(f'Если у организации убыток, то значение со знаком минус и в расчете средней прибыли не учитывается \n'
      f'{res_list}')
with open('companies.json', 'w') as f_json:
    json.dump(res_list, f_json)
# Проверим, что достанется из json-файла
with open('companies.json') as f_json:
    res_list = json.load(f_json)
print(f'Этот словарь достан из недр "companies.json" \n'
      f'{res_list}')