# Object oriented Programming

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def set_age(self, age):  # Modifying attributes
        self.age = age
    # def add_one(self, x):
    #     return x + 1
    # def bark(self):
    #     print("bark")


# creating a new instance of the class dog
d = Dog("Merlin", 12)
d.set_age(52)
print(d.get_name(), "is ", d.get_age(), " years old")
d2 = Dog("Biden", 13)
d2.set_age(65)
print(d2.get_name(), "is ", d2.get_age(), " years old")


# d.bark()
# print(d.add_one(5))

# Learning to create Multiple Classes

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade  # 0 - 100

    def get_grade(self):  # Method that returns  the students grade
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()


# Adding Students to the courses
s1 = ("Ronald", 17, 95)
s2 = ("Benita", 19, 98)
s3 = ("Ayomide", 24, 99)
s4 = ("Sharon", 22, 92)
s5 = ("Tofunmi", 20, 90)

course = Course("Science", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s5)
course.add_student(s4)
course.add_student(s3)

print(course.students)
