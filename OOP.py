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

        return value // len(self.students)


# Creating instances of the Student class
s1 = Student("Ronald", 17, 95)
s2 = Student("Benita", 19, 98)
s3 = Student("Ayomide", 24, 99)
s4 = Student("Sharon", 22, 92)
s5 = Student("Tofunmi", 20, 90)

# Creating a course instance and adding students to it
course = Course("Science", 3)
course.add_student(s1)
course.add_student(s2)
course.add_student(s5)
course.add_student(s4)
course.add_student(s3)

print(course.get_average_grade())


# Understanding Inheritance

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print("My name is", self.name, "and i am", self.age, "Years old")

    def speak(self):
        print("I dont know what to say")


class Cat(Pet):
    # using super init to get inheritance
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print("My name is", self.name, "and i am", self.age, "Years old and i am ", self.color)


class Hen(Pet):

    def speak(self):
        print("Crow")


class Fish(Pet):
    pass


p = Pet("Jack", 16)
p.show()
p.speak()

c = Cat("Tom", 20, "brown")
c.show()
c.speak()

h = Hen("Jerry", 35)
h.show()
h.speak()

f = Fish("Octopus", 18)
f.show()
f.speak()


# CLASS ATTRIBUTES
# Class attributes are attributes that are specific to a class.
# Not to an instance of that class or to an object of that class

class Person:
    number_of_person = 0
    GRAVITY = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod
    def number_of_person(cls):
        return cls.number_of_person

    @classmethod
    def add_person(cls):
        cls.number_of_person += 1


# p1 = Person("deola")
# print(p1.number_of_person)
# p2 = Person("sharon")
# print(p2.number_of_person)
print(Person.number_of_person())
