class Transport:
    def __init__(self, year, model, color, penalties=0):
        self.year = year 
        self.model = model  
        self.color = color  
        self.penalties = penalties
    
    def change_color(self, new_color):
        self.color = new_color
        
    def drive(self, city):
        print(f'Car {self.model} is driving to {city}')

class Plane(Transport):
    def __init__(self, year, model, color):
        super().__init__(year, model, color)


class Car(Transport):
    #атрибут класса
    counter = 0
    wheels_num_by_standart = 5

    #конструктор
    def __init__ (self, year, model, color, penalties=0): #входящие параметры
        #поля/атрибуты
        super().__init__(year, model, color ) 
        self.penalties = penalties
        Car.counter += 1

    

class Truck(Transport):
    def __init__(self, year, model, color, penalties=0, load_capacity=35000):
        super().__init__(year, model, color, penalties)
        self.load_capacity = load_capacity
    

    def load_cargo(self, weight, type):
        if weight > self.load_capacity:
            print(f'You can not load more than {self.load_capacity}')
        else:
            print(f'Cargo of {type} was successfully loaded on {self.model}')
 #методы
    

prise_of_lastis = 5000

#ссылочная переменная
bmw_car = Car( 2020, 'BMW X6', 'Red' , 0) 
print(f'YEAR: {bmw_car.year} MODEL: {bmw_car.model}'
      f' COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')
# bmw_car.color = 'Black' #через такой метод поменяли цвет машины
bmw_car.change_color('Black')
print(f'YEAR: {bmw_car.year} MODEL: {bmw_car.model}'
      f' NEW COLOR: {bmw_car.color} PENALTIES: {bmw_car.penalties}')

honda_car = Car(2011, 'Accord', 'Grey', 2500)
print(f'YEAR: {honda_car.year} MODEL: {honda_car.model}'
      f' COLOR: {honda_car.color} PENALTIES: {honda_car.penalties}') 

honda_car.drive('Osh')

print(f'Мы произвели {Car.counter} машин')
print(f'Нам нужно {prise_of_lastis * Car.wheels_num_by_standart * Car.counter} сом , чтобы купить зимние шины')

boeing = Plane(2022, 'Boeing-747', 'Blue')
print(f'YEAR: {boeing.year} MODEL: {boeing.model}'
      f' COLOR: {boeing.color}')

daf_truck = Truck(2009, 'Daf-33', 'White', 5000, 35000)
print(f'YEAR: {daf_truck.year} MODEL: {daf_truck.model}'
      f' COLOR: {daf_truck.color} PENALTIES: {daf_truck.penalties}' 
      f' LOAD CAPACITY: {daf_truck.load_capacity} kg')

daf_truck.load_cargo(20000, 'Banana')
daf_truck.drive('Naryn')