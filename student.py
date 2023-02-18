from facultet import Facultet


class Student:
    def __init__(self, name: str, age: int, facultet: Facultet):
        self.name = name
        self.age = age
        self.facultet = facultet.name

    def __str__(self):
        return f"{self.name}, {self.age}, {self.facultet}."

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.facultet}."

    def study(self, subject: str):
        print(f"{self.name} study {subject}")
