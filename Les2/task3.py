user_month = int(input('Enter number of month from 1 to 12: '))
months = ['january', 'february', 'march', 'april', 'may', 'june', 'jule', 'august',
          'september', 'october', 'november', 'december']
months_dict = {1 : 'january', 2 : 'february', 3 : 'march', 4 : 'april', 5 : 'may', 6: 'june', 7: 'jule', 8: 'august',
               9: 'september', 10 : 'october', 11 : 'november', 12 : 'december'}
seasons = ['winter', 'spring', 'summer', 'autumn']
seasons_dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
# не совсем уловил суть задания, но выберем все из словарей и списков. Сначала списки, потом словари.
print(f'Month №{user_month} calls {months[user_month-1]}, that means {seasons[user_month//4]}')
print(f'Month №{user_month} calls {months_dict[user_month]}, that means {seasons_dict[user_month//4 + 1]}')