# Проверяем вначале попадает число вне или равно максимуму или минимуму (например 25, 11, 2 или 1), потом есть ли оно в
# списке (например 7), потом, ищем ячейку делением списка пополам, чтоб в итоге справа было число меньше, а слева число
# больше. Так для числа 9 найдется место между 11 и 8. Все варианты оттестированы.
rating_list = [11, 11, 8, 7, 7, 7, 6, 5, 5, 4, 3, 2, 2]
print(f"It's our rating list {rating_list}")
user_number = int(input('Enter natural number: '))
place_max = 0
place_min = len(rating_list) - 1
if user_number >= rating_list[place_max]:
    rating_list.insert(place_max, user_number)
elif user_number <= rating_list[place_min]:
    rating_list.insert(place_min + 1, user_number)
elif user_number in rating_list:
    rating_list.insert(rating_list.index(user_number), user_number)
else:
    place = (place_max + place_min) // 2
    while not (user_number < rating_list[place] and user_number > rating_list[place+1]):
        if user_number < rating_list[place]:
            place_max = place
        else:
            place_min = place
        place = (place_max + place_min) // 2
    rating_list.insert(place+1, user_number)
print(f"It's our new rating list {rating_list}")

