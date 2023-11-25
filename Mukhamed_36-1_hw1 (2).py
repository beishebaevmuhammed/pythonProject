"""
#ДЗУрок1 ДЭДЛАЙН 05.11.2023 23 59
ДЗ*:
1. Создать класс Person с атрибутами fullname, age, is_married
2. Добавить в класс Person метод introduce_myself, который бы распечатывал всю информацию о человеке
3. Создать класс Student наследовать его от класса Person и дополнить его атрибутом marks, который 
   был бы словарем, где ключ это название урока, а значение - оценка.
4. Добавить метод в класс Student, который бы подсчитывал среднюю оценку ученика по всем предметам
5. Создать класс Teacher и наследовать его от класса Person, дополнить атрибутом experience. 
6. Добавить в класс Teacher атрибут уровня класса base_salary
7. Также добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: 
   к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3-х лет.
8. Создать объект учителя и распечатать всю информацию о нем и высчитать зарплату
9. Написать функцию create_students, в которой создается 3 объекта ученика, эти ученики добавляются в список 
   и список возвращается функцией как результат.
10. Вызвать функцию create_students и через цикл распечатать всю информацию о каждом ученике 
    с его оценками по каждому предмету. Также рассчитать его среднюю оценку по всем предметам.
"""

class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'FULLNAME: {self.fullname} AGE:{self.age}' 
              f'IS_MARRIED{self.is_married}')

class Student(Person):
    def __init__(self, fullname, age, is_married, marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks
      
    def calculate_average_mark(self):
        total_marks = sum(self.marks.values())
        num_subjects = len(self.marks)
        return total_marks / num_subjects
    
#добавить метод в класс Teacher, который бы считал зарплату по следующей формуле: 
#к стандартной зарплате прибавляется бонус 5% за каждый год опыта свыше 3-х лет.
class Teacher(Person):
    
    base_salary = 0

    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)
        self.experience = experience

    def calculate_salary(self):
      bonus_percentage = max(0,(self.experience - 3)*5)
      bonus = self.self.base_salary * (bonus_percentage / 100)
      total_salary = self.base_salary + bonus
      return total_salary
    

teacher=Teacher('Aleksei', 35, True, '15 y.')
teacher.calculate_salary
print(f'')
      



