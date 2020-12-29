user_number = input('Введите число: ')
user_number_x_2 = user_number+user_number
user_number_x_3 = user_number_x_2+user_number
# Ниже print разнесен на 3 строки, чтобы было удобно читать вместо бесконечной строки.
# Насколько это оправдано и стоит ли так делать, не знаю. Буду рад комментарию.
print(f'{user_number} - ваше число\n'
      f'{user_number_x_2} - ваше число, к которому приписали его же еще раз\n'
      f'{user_number_x_3} - ваше число, к которому приписали его же дважды')
print(f'{int(user_number)+int(user_number_x_2)+int(user_number_x_3)} - сумма сего странного набора ')