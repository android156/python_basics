from itertools import count

with open('user_text.txt', 'w', encoding='utf-8') as f:
    for i in count(1):
        part_text = input(f'Введите строку №{i} для записи в файл, "Enter" - запись в файл, переход\n'
                          f'к следующей строке. Для окончания просто "Enter" после пустой строки:\n')
        if part_text == '':
            break
        else:
            f.write(part_text + '\n')
            print(f'Строка {i} записана')
print('файл закрыт - ',f.closed)