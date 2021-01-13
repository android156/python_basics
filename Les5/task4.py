digit_dict = {'One' : 'Один',
              'Two' : 'Два',
              'Three' : 'Три',
              'Four' : 'Четыре',
              'Five' : 'Пять',
              'Six' : 'Шесть',}
# Словарь можно продолжить и перевести любые цифры
with open('onetwothree.txt', encoding='utf-8') as f:
    with open('одиндватри.txt', 'w', encoding='utf-8') as f_res:
        for line in f.readlines():
            print(line.strip())
            print(line.split())
            line_list = line.split()
            line_list[0] = digit_dict[line_list[0]]
            print(' '.join(line_list), file=f_res)

