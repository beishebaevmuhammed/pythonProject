# function, аргументы: *args, **kwargs
# DRY - dont repeat yourself
# def - define



# def get_fullname(name, surname='неизвестно'): #name = обязательный позиционный параметр
#     return ('имя:', name.upper(), 'фамилия:', surname.upper())
# print(get_fullname("Мухаммед", "Бейшебаев"))#Мухаммед-является о.п.а)
# print(get_fullname("Karl", "Jackson"))
# print(get_fullname(surname="Володьев", name="Кеша")) #- keyword arguments - ключевой аргумент)
# print(get_fullname('Григорий'))

# print(len.__doc__)

'''
определение, наименование(параметры):
    тело функции
    возвращение результата

вызов функции
наименование(аргументы)
'''


# def get_square(width, lenght):
"""
     вводя функию def мы даем наименование, в нашем случае get_square,
     внутри наименования параметры (ширина и длина)
"""
#     result = width * lenght
#     return result
# print(type(get_square.__doc__))
# print(dir(get_square))
# square_victory = get_square(200, 500)
# print(square_victory)

# width = 5
# lenght = 8
# sq_2 = width * lenght
# print(sq_2)

# width = 200
# lenght = 500
# square_victory = width * lenght
# print(square_victory)

# num = [1, 9, 2, 8, 3, 7, 4, 6, 5]
# def max1(sequence):
#     max_value = sequence[0]
#     for num in sequence:
#         print(num, max_value)
#         if num > max_value
#             max_value = num
#     return max_value
# print(max1(num))

# def plus(*args):
#     return sum(args)
# print(plus(5, 4, 3, 2))
#
# def menu(**kwargs):
#     return kwargs
# monday = menu(eat='pizza', drink='cola')
# print(monday)

# def is_even_odd(number):
#     if not isinstance(number, int):
#         return None
#     return number % 2 == 0
# print(is_even_odd(4))  # True
# print(is_even_odd(7))  # False
# print(is_even_odd(2.5))  # None

def get_aaa(predlojenie):
    # Проверяем, начинается ли предложение с заглавной буквы и заканчивается точкой
    if predlojenie[0].isupper() and predlojenie[-1] == '.':
        return True
    else:
        return False

# Пример использования функции
predlojenie1 = "Это предложение корректно."
predlojenie2 = "Это все правда."
result1 = get_aaa(predlojenie1)
result2 = get_aaa(predlojenie2)

print(result1)  # Вывод: True
print(result2)  # Вывод: False



