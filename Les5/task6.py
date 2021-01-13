res_dict = {}
print(f'Строки из файла "classes.txt":\n')
with open('classes.txt', encoding='utf-8') as f:
    for line in f.readlines():
        print(line.strip())
        list_line = line.split()
        new_list = []  # Сюда будем записывать только числа из каждой строки
        for i, el in enumerate(list_line):  # enumerate нужен исключительно чтобы отделить первый(0) элемент
            if i > 0:
                new_el = ''
                for digit in el:  # Все, что цифра в каждом слове кидаем в новый элемент
                    if digit.isdigit():
                        new_el += digit
                if new_el != '':    # Если не мусор, то добавить число в новый список
                    new_list.append(new_el)
        res_dict[list_line[0][:len(list_line[0])-1]] = sum(map(int, new_list))
        #  убрали ":" и присвоили первому элементу сумму всех чисел в первой строке
print(f'\nПолученный словарь\n{res_dict}')
