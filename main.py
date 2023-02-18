from facultet import Facultet
from student import Student


list=[]
facultet = Facultet("NNIKNUP", list)
student1 = Student("Andrey", 20, facultet)
list.append(student1)
def add(name: str, age:int, facultet:Facultet):
    list.append(Student(name, age, facultet))
print("Если ты хочешь добавить студента напиши; 1")
print("Вывести список студентов напиши: 2")
a = input("Введите ваш выбор: ")
if(int (a) == 1):
    print("Введите имя")
    name = input()
    print("Введите возраст")
    age = input()
    add(name, age, facultet)
    print(list)
elif(int (a) == 2):
    print(list)






