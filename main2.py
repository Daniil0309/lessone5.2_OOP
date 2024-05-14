#Агрегация
class Teacher():
    def teach(self):
        print("Учитель учит")

class School():
    def __init__(self, new_teacher): #2.Передали обьект класса 1 в этот класс
        self.teacher = new_teacher
    def start_lesson(self):
        self.teacher.teach() #3.вызвали метод учителя

my_teacher = Teacher() #1.создали отдельный обьект класса учитель
my_school = School(my_teacher)
