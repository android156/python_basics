def get_part_sum():
    str_numbers = input(': ')
    list_numbers = str_numbers.split()
    list_numbers.reverse()
    f_sum = 0
    q_trigger = True if list_numbers[0] == 'Q' else False# тернарный оператор применен дважды)))
    if q_trigger:
        list_numbers.remove('Q')
    if len(list_numbers) > 0:
        for i in range(len(list_numbers)):
            list_numbers[i] = float(list_numbers[i])
        f_sum = sum(list_numbers)
    return f_sum, q_trigger

print('Вводите числа через пробел, если хотите увидеть\n'
      'промежуточную сумму, нажмите "Enter", если все \n'
      'ввели, введите "Q"')
stop = False
part_result = 0
result = 0
while stop == False:
    part_result, stop = get_part_sum()
    result += part_result
    print(f'Промежуточная сумма: {result}') if stop == False  else print(f'Cумма всех чисел: {result}')
    # тернарный оператор

