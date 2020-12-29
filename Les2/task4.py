user_string = input('Enter any text in one line: ')
user_list = user_string.split()
for number, word in enumerate(user_list, 1):
    print(number, word[:10])
# Я бы усложнил и выкинул бы все предлоги)))