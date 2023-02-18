class Facultet:
    def __init__(self, name: str, students=[]):
        self.name = name
        self.students = students

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"