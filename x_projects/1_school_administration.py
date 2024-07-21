class Adress:
    def __init__(self, country: str, city: str, PLZ: int, street: str, number: int):
        self.country = country
        self.city = city
        self.PLZ = PLZ
        self.street = street
        self.number = number

    def __repr__(self):
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
        self.grades: dict[str, float] = {}
    
    def assign_grade(self, subject: str, grade: float):
        self.grades[subject] = grade

    def get_grades(self) -> dict[str, float]:
        return self.grades

    def get_average_grade(self):
        if not self.grades:
            return 0.0
        return sum(self.grades.values()) / len(self.grades)

class Teacher(Person):
    def __init__(self, name: str, age: int, adress: Adress, phone_number: int, email: str):
        super().__init__(name, age, adress, phone_number, email)
        self.subjects: list[str] = []
        self.students: dict[str, list[Student]] = {}

    def add_subject(self, subject: str):
        if subject not in self.subjects:
            self.subjects.append(subject)
            self.students[subject] = []
    
    def add_student_to_subject(self, student: Student, subject: str):
        if subject in self.subjects:
            self.students[subject].append(student)

    def assign_grade(self, student: Student, subject: str, grade: float):
        if subject in self.subjects and student in self.students[subject]:
            student.assign_grade(subject, grade)

    def get_subject_students(self, subject: str):
        return self.students.get(subject, [])

    def list_subjects(self):
        return self.subjects
    
    def get_students_avarage_grade(self):
        grades_count = 0
        grades_sum = 0

        for subject, students in self.students.items():
            for student in students:
                grades_count += 1
                grades: dict[str, float] =  student.get_grades()
                grades_sum += grades[subject]
        if grades_count == 0:
            return 0
        return grades_sum / grades_count


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


def main():
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

    Hanna.add_subject("Mathematik")
    Hanna.add_subject("Deutsch")
    Hanna.add_student_to_subject(Hans, "Mathematik")
    Hanna.add_student_to_subject(Hans, "Deutsch")
    Hanna.add_student_to_subject(Lara, "Mathematik")
    Hanna.add_student_to_subject(Mark, "Deutsch")
    Hanna.add_student_to_subject(Luise, "Deutsch")

    Hanna.assign_grade(Hans, "Mathematik", 10.0)
    Hanna.assign_grade(Hans, "Deutsch", 22.0)
    Hanna.assign_grade(Lara, "Mathematik", 0.0)
    Hanna.assign_grade(Mark, "Deutsch", 5.0)
    Hanna.assign_grade(Luise, "Deutsch", 2.0)

    print(Hanna.get_students_avarage_grade())


if __name__ == "__main__":
    main()