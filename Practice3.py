# Создайте класс Author и класс Book. Класс Book должен использовать композицию для включения автора в качестве объекта.

# Определение класса Author (Автор)
class Author():
    # Конструктор класса, принимающий имя и национальность автора
    def __init__(self, name, nationality):
        self.name = name  # Инициализация атрибута name
        self.nationality = nationality  # Инициализация атрибута nationality

# Определение класса Book (Книга)
class Book():
    # Конструктор класса, принимающий название книги и объект автора
    def __init__(self, title, author):
        self.title = title  # Инициализация атрибута title
        self.author = author  # Инициализация атрибута author

    # Метод для получения информации о книге
    def get_info_book(self):
        # Вывод названия книги и имени автора на экран
        print(f"{self.title} - {self.author.name}")

# Создание экземпляра класса Author с именем "Лев Толстой" и национальностью "Русский"
author = Author("Лев Толстой", "Русский")

# Создание экземпляра класса Book с названием "Война и мир" и объектом автора "Лев Толстой"
book = Book("Война и мир", author)

# Вывод имени автора на экран
print(author.name) #композиция

# Вызов метода get_info_book объекта book для получения информации о книге
book.get_info_book()