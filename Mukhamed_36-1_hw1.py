Monday = float(input('введите расход за понедельник: '))
Tuesday = float(input('введите расход за вторник: '))
Wednesday = float(input('введите расход за среду: '))
Thursday = float(input('введите расход за четверг: '))
Friday = float(input('введите расход за пятницу: '))
Saturday = float(input('введите расход за субботу: '))
Sunday = float(input('введите расход за воскресенье: '))
Summa = Monday+Tuesday+Wednesday+Thursday+Friday+Saturday+Sunday
Average_expenses = Summa / 7
print(f'Общий расход за неделю: {Summa}')
print(f'Средние расходы за неделю: {round(Average_expenses, 1)}')



