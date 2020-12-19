sec_time = int(input('Введите время в секундах - '))
hours = sec_time // 3600
mins = (sec_time % 3600) // 60
secs = sec_time % 60
print(f'Если перевести {sec_time} секунд в часы минуты и секунды, то получится \n {hours} часов,  {mins} минут и {secs} секунд')