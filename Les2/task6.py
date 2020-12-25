storage = [
    (1, {"name":"desktop", "price":"2000", "quantity":20, "measure":"unit"}),
    (2, {"name":"printer", "price":"300", "quantity":10, "measure":"unit"}),
    (3, {"name":"scaner", "price":"500", "quantity":17, "measure":"unit"})
]
empty_dict = {"name":"", "price":"", "quantity":0, "measure":""}

print(f'Сейчас будем вводить товары и характеристики через\n'
      f'пробел так: название цена кол-во единица измерения \n'
      f'Пример "Носки 200 20 пара" \n'
      f'после ввода каждого элемента жмем клавишу "Enter",\n'
      f'Когда все товары введены, пишем "хватит" без кавычек\n')
user_storage = []
product_parameters = {"name": "", "price": "", "quantity": 0, "measure": ""}
product_count = 0
while True:
    product_count += 1
    element = input(f'Введите {product_count}-й товар: ')
    if element != 'хватит':
        element_list = element.split()
        product_parameters["name"] = element_list[0]
        product_parameters["price"] = element_list[1]
        product_parameters["quantity"] = element_list[2]
        product_parameters["measure"] = element_list[3]
        product = (product_count, product_parameters.copy()) #Пока до этого .copy допер, уже застрелиться хотел
        # Словил словари в кортежах, вроде добавляю следующий с параметрами новой вещи,
        # а меняются все предыдущие на последний. И тут я вспомнил про адрес ячейки и копирование
        user_storage.append(product)
    else:
        break
print(f'вся база \n {user_storage}')
# user_storage = storage Использовал для теста.
name_list = []
price_list = []
quantity_list = []
measure_list = []
storage_analitics = {}
for el in user_storage:
    name_list.append(el[1]['name'])
    price_list.append(el[1]['price'])
    quantity_list.append(el[1]['quantity'])
    measure_list.append(el[1]['measure'])
storage_analitics['name'] = name_list
storage_analitics['price'] = price_list
storage_analitics['quantity'] = quantity_list
storage_analitics['measure'] = measure_list
print(f'Аналитика \n {storage_analitics}')