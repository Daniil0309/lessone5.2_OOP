# #Дополнительно:
# Попробуйте добавить дополнительные функции в вашу программу, такие как сохранение информации о зоопарке в файл
# и возможность её загрузки, чтобы у вашего зоопарка было "постоянное состояние" между запусками программы.

import pickle

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def save(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)

    @staticmethod
    def load(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

# Создаем экземпляр зоопарка
zoo = Zoo("Зоопарк")

# Добавляем животных и сотрудников
hare = Animal("Рыжик", "Заяц")
horse = Animal("Ягуар", "Лошадь")
zoo.add_animal(hare)
zoo.add_animal(horse)

security = Employee("Даниил", "Охраник")
veterinarian = Employee("Мария", "Ветеринар")
zoo.add_employee(security)
zoo.add_employee(veterinarian)

# Сохраняем состояние зоопарка в файл
zoo.save("zoo.pkl")

# Загружаем состояние зоопарка из файла
new_zoo = Zoo.load("zoo.pkl")

# Проверяем, что состояние загружено корректно
print("Загруженное название зоопарка:", new_zoo.name)
print("Животные в зоопарке:")
for animal in new_zoo.animals:
    print(animal.name, "-", animal.species)
print("Сотрудники зоопарка:")
for employee in new_zoo.employees:
    print(employee.name, "-", employee.position)
