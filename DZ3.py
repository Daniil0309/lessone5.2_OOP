#3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных
# и вызывает метод `make_sound()` для каждого животного.

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Bird(Animal):
    def __init__(self, name, age, wingspan):
        super().__init__(name, age)
        self.wingspan = wingspan

    def make_sound(self):
        print(f"{self.name} щебечет.")
class Mammal(Animal):
    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print(f"{self.name} рычит.")

class Reptile(Animal):
    def __init__(self, name, age, skin_color):
        super().__init__(name, age)
        self.skin_color = skin_color

    def make_sound(self):
        print(f"{self.name} кричит.")

def animal_sound(animals):
    for animal in animals:
        animal.make_sound()

bird = Bird("Попугай", 3, 20.5)
mammal = Mammal("Кот", 5, "Белый")
reptile = Reptile("Змейка", 2, "Зелый")

animals = [bird, mammal, reptile]

animal_sound(animals)

