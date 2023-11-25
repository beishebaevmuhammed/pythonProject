"""Счетчик гласных и согласных букв
1.Программа должна работать в цикле while с возможностью выхода (break)
2.Запрашивать у пользователя любое слово на латинице или кириллице (рус, анг)
3.Считывать строчные и прописные буквы (большие, маленькие)
4.Вывести общее количество букв в данном слове
5.Вывести количество согласных и гласных букв
6.Вывести процентное соотношение гласных и согласных букв до двух цифр после точки"""

glas = 'aeiouyаеоуыёюиэ'

while True:
    glas1 = 0
    soglas = 0
    word = input("Введите слово: ")
    word_length = len(word)
    if word.lower() == "выход":
        break
    for i in word:
        if i.lower() in glas:
            glas1 += 1
        else:
            soglas += 1
    vowel_percentage = (glas1 / word_length ) * 100
    consonant_percentage = (soglas / word_length) * 100
    print("Слово: ", word)
    print("Согласных букв: ", soglas)
    print("Гласных букв: ", glas1)
    print(f"Гласные/Согласные: {round(consonant_percentage, 2)}% / {round(vowel_percentage, 2)}%")