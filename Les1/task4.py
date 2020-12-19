user_number = input('Введите число: ')
print(f'Если Вы ввели число без опечаток, то в нем {len(user_number)} цифр')
max_digit = 0
count = 0
while count < len(user_number):
    if int(user_number[count]) > max_digit:
        max_digit = int(user_number[count])
    count += 1
print(f'{max_digit} - максимальная цифра в веденном числе')

