# Object oriented Programming

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # def add_one(self, x):
    #     return x + 1
    # def bark(self):
    #     print("bark")


# creating a new instance of the class dog
d = Dog("Merlin", 12)
print(d.get_name(), "is ", d.get_age(), " years old")
d2 = Dog("Biden", 13)
print(d2.get_name(), "is ", d2.get_age(), " years old")
# d.bark()
# print(d.add_one(5))
