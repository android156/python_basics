print(f'Сейчас будем вводить элементы списка по очереди, \n'
      f'после ввода каждого элемента, жмем клавишу "Enter",\n'
      f'а как надоест, напишите слово "хватит" без кавычек\n')
user_list = []
count = 0
while True:
    count += 1
    element = input(f'Введите {count}-й элемент списка: ')
    if element != 'хватит':
        user_list.append(element)
    else:
        break
print(f'Введенный список: {user_list}')
for i in range(len(user_list)//2):
    user_list[i*2], user_list[i*2 + 1] = user_list[i*2 + 1], user_list[i*2]
print(f'Список измененный: {user_list}')
