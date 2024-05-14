# Задача №2 с использованием полиморфизма.
# Продемонстрировать принцип полиморфизма через реализацию разных классов, представляющих геометрические формы, и метод для расчёта площади каждой формы.
# Создать базовый класс Shape с методом area(), который просто возвращает 0.
# Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square), каждый из которых переопределяет метод area().
# В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# Написать функцию, которая принимает объект класса Shape и выводит его площадь.

# Определение базового класса Shape (Фигура)
class Shape:
    # Метод area возвращает площадь фигуры, который будет переопределен в подклассах
    def area(self):
        return 0


# Определение подкласса Circle (Круг), который наследует от класса Shape
class Circle(Shape):
    # Конструктор класса Circle, который принимает радиус круга
    def __init__(self, radius):
        self.radius = radius

    # Переопределение метода area для вычисления площади круга
    def area(self):
        return 3.14 * self.radius ** 2


# Определение подкласса Rectangle (Прямоугольник), который наследует от класса Shape
class Rectangle(Shape):
    # Конструктор класса Rectangle, который принимает ширину и высоту прямоугольника
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # Переопределение метода area для вычисления площади прямоугольника
    def area(self):
        return self.width * self.height


# Определение подкласса Square (Квадрат), который наследует от класса Shape
class Square(Shape):
    # Конструктор класса Square, который принимает длину стороны квадрата
    def __init__(self, width):
        self.width = width

    # Переопределение метода area для вычисления площади квадрата
    def area(self):
        return self.width * self.width


# Функция print_area, которая принимает объект фигуры и выводит его площадь
def print_area(shape):
    print(f"Площадь - {shape.area()}")


# Создание экземпляров классов Circle, Square и Rectangle
circle = Circle(5)
square = Square(7)
rectangle = Rectangle(10, 20)

# Вывод площади каждой фигуры с помощью функции print_area
print_area(circle)
print_area(square)
print_area(rectangle)