# работа с файлами
# x - создание файла
# w - write
# a - add

# file = open('new_file.txt', 'w')
# file.write('Какая-то информация!(Писать на кириллице)')
# file.close()

# with open('new_file.txt', 'a')as file:
#     file.write('second str #2(vtoraya stroka)')

# with open('new_file1.txt', 'x')as file:
#     file.write('new data!')

# with open('new_file.txt', 'r')as file:
#     print(file.read())

students = [5, 16, 11, 13, 1, 6, 19, 15, 4, 20, 12, 9, 2, 10, 17, 8]

with open('results.txt','x') as balls:
    balls.write('results test #1 gr 36-1\n\n'.upper())

while students:
    name = input(f'введите имя студента под номером:  {students[0]}').title()
    rate = input(f'введите оценку:  {name}')
    with open('results.txt', 'a') as results:
        results.write(f'{name} {rate}\n')
        del students[0]
        print(students)