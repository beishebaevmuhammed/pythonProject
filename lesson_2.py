class Animal:
    def __init__(self, name, age):
        self.__name = name
        if type(age) == int and age > 0:
            self.__age = age 
        else:
            raise ValueError('Wrong value for attribute age. It must be positive number ')
        


    def get_age(self):
        return self.__age
    
    def get_name(self):
        return self.__name
    
    def set_name(self, new_name):
        self.__name = new_name

    

    def set_age(self, new_age):
        if type(new_age) == int and new_age > 0:
            self.__age = new_age 
        else:
            raise ValueError('Wrong value for attribute age. It must be positive number ')

    def info(self):
        return f'NAME:{self.__name} AGE:{self.__age} BIRTH YEAR {2023 - self.__age} '


some_animal = Animal('Anim', 7)
print(some_animal.info())
some_animal.set_age(4)
print(some_animal.info())
print(some_animal.get_name())



