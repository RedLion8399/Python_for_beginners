class Adress:
    def __init__(self, country: str, city: str, PLZ: int, street: str, number: int):
        self.country = country
        self.city = city
        self.PLZ = PLZ
        self.street = street
        self.number = number

    def __str__(self):
        return f"{self.street} {self.number}, {self.PLZ} {self.city}, {self.country}"


class Person:
    def __init__(self, name: str, age: int, adress: Adress, phone_number: int, email: str):
        self.name = name
        self.age = age
        self.adress = adress
        self.phone_number = phone_number
        self.email = email

    
    def birthday(self):
        self.age += 1
        print(f"Happy birthday {self.name}! You are now {self.age} years old.")


class Student(Person):
    def __init__(self, name: str, age: int, adress: Adress, phone_number: int, email: str):
        super().__init__(name, age, adress, phone_number, email)
    

class Teacher(Person):
    def __init__(self, name: str, age: int, adress: Adress, phone_number: int, email: str):
        super().__init__(name, age, adress, phone_number, email)


class School:
    def __init__(self, name: str):
        self.name = name
        self.students: list[Student] = []
        self.teachers: list[Teacher] = []

    def add_student(self, student: Student):
        self.students.append(student)

    def add_teacher(self, teacher: Teacher):
        self.teachers.append(teacher)

    def get_student(self, name: str):
        for student in self.students:
            if student.name == name:
                return student

    def get_teacher(self, name: str):
        for teacher in self.teachers:
            if teacher.name == name:
                return teacher


# Test

s = School("Hauptstadt")

Hans = Student("Hans", 12, Adress("Schweiz", "Zug", 6300, "Hauptstrasse", 1), 123456789, "hans@me.com")
Lara = Student("Lara", 12, Adress("Schweiz", "Zug", 6300, "Hauptstrasse", 1), 123456789, "lara@me.com")
Mark = Student("Mark", 12, Adress("Schweiz", "Zug", 6300, "Hauptstrasse", 1), 123456789, "mark@me.com")
Luise = Student("Luise", 12, Adress("Schweiz", "Zug", 6300, "Hauptstrasse", 1), 123456789, "luise@me.com")

Hanna = Teacher("Hanna", 45, Adress("Schweiz", "Zug", 6300, "Hauptstrasse", 1), 123456789, "hanna@me.com")
Jan = Teacher("Jan", 45, Adress("Schweiz", "Zug", 6300, "Hauptstrasse", 1), 123456789, "jan@me.com")

s.add_student(Hans)
s.add_student(Lara)
s.add_student(Mark)
s.add_student(Luise)
s.add_teacher(Hanna)