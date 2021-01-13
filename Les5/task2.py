# Будем использовать файл созданный в предыдущем задании user_text.txt

with open('user_text.txt', encoding='utf-8') as f:
    for i, line in enumerate(f.readlines(), start=1):
        print (f'строка №{i} "{line.strip()}" - {len(line.split())} слов')
