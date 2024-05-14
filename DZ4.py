#4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках.
# Должны быть методы для добавления животных и сотрудников в зоопарк.

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Employee():
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Zoo():
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

zoo = Zoo("Зоопарк")

hare = Animal("Рыжик", "Заяц")
horse = Animal("Ягуар", "Лошадь")
zoo.add_animal(hare)
zoo.add_animal(horse)

security = Employee("Даниил", "Охраник")
veterinarian = Employee("Мария", "Ветеринар")
zoo.add_employee(security)
zoo.add_employee(veterinarian)
