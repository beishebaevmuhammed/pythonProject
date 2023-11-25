

day = int(input('Введите день своего рождения: '))
month = int(input('Введите месяц своего рождения: '))
if (month == 3 and day >= 21 and day <= 31) or (month == 4 and day <= 20):
    print('Вы Овен')
elif (month == 4 and day >= 21 and day <= 30) or (month == 5 and day <= 21):
    print('Вы Телец')
elif (month == 5 and day >= 22 and day <= 31) or (month == 6 and day <= 21):
    print('Вы Близнецы')
elif (month == 6 and day >= 22 and day <= 30) or (month == 7 and day <= 22):
    print('Вы Рак')
elif (month == 7 and day >= 23 and day <= 31 ) or (month == 8 and day <= 21):
    print('Вы Лев')
elif (month == 8 and day >= 22 and day <= 31) or (month == 9 and day <= 23):
    print('Вы Дева')
elif (month == 9 and day >= 24 and day <= 30) or (month == 10 and day <= 23):
    print('Вы Весы')
elif (month == 10 and day >= 24 and day <= 31 ) or (month == 11 and day <= 22):
    print('Вы Скорпион')
elif (month == 11 and day >= 23 and day <= 30 ) or (month == 12 and day <= 22):
    print('Вы Стрелец')
elif (month == 12 and day >= 23 and day <= 31 ) or (month == 1 and day <= 20):
    print('Вы Козерог')
elif (month == 1 and day >= 21 and day <= 31 ) or (month == 2 and day <= 19):
    print('Вы Водолей')
elif (month == 2 and day >= 20 and day <=29 ) or (month == 3 and day <= 20):
    print('Вы Рыбы')
else:
    print('Некорректная дата рождения!')
