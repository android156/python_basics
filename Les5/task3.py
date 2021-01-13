all_salary_list = []
happy_list = []
happy_salary_list = []
with open('salaries.txt', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())
        if int(line.split()[1]) >= 20000:
            happy_list.append(line.split()[0])
            happy_salary_list.append(int(line.split()[1]))
        all_salary_list.append(int(line.split()[1]))
print (f'Cредняя зарплата всех сотрудников {round(sum(all_salary_list)/len(all_salary_list))}\n'
       f'Список счастливчиков с ЗП >= 20000 {happy_list}\n'
       f'Cредняя зарплата всех счастливчиков {round(sum(happy_salary_list)/len(happy_salary_list))}')