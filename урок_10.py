'''

'''
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f'Name: {self.name} Age: {self.age} Birth year: {2023 - self.age} '
some_animal = Animal (name= 'Anim', age= 2)
print(some_animal.info)

