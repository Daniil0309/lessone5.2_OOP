#5.Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы
# (например, `feed_animal()` для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, name, species):
        self.name = name
        self.species = species

class Security():
    def __init__(self, name):
        self.name = name
    def feed_animal(self, animal):
        print(f"{self.name} покормил {animal.species}.")

class Veterinarian():
    def __init__(self, name):
        self.name = name
    def heal_animal(self, animal):
        print(f"{self.name} лечил {animal.species}.")


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

security = Security("Даниил")
veterinarian = Veterinarian("Мария")
zoo.add_employee(security)
zoo.add_employee(veterinarian)

for animal in zoo.animals:
    security.feed_animal(animal)

for animal in zoo.animals:
    veterinarian.heal_animal(animal)