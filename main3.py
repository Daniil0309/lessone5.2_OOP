#Полиморфизм

# Определение класса Dog (Собака)
class Dog():
    # Метод для издания звука, характерного для собаки
    def speak(self):
        return "Гав"

# Определение класса Cat (Кошка)
class Cat():
    # Метод для издания звука, характерного для кошки
    def speak(self):
        return "Мяу"

# Функция для вызова метода speak объекта, не зависящего от конкретного типа животного
def animal_speak(animal):
    print(animal.speak())  # Вызов метода speak объекта animal

# Создание экземпляра класса Dog с именем dog
dog = Dog()
# Создание экземпляра класса Cat с именем cat
cat = Cat()

# Вызов функции animal_speak с объектом dog в качестве аргумента
animal_speak(dog)
# Вызов функции animal_speak с объектом cat в качестве аргумента
animal_speak(cat)