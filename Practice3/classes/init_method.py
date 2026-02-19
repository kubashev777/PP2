class Person:
    def __init__(self, name):
        self.name = name

p1 = Person("Alice")
print(p1.name)


class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c1 = Car("BMW", 2022)
print(c1.brand, c1.year)


class Student:
    def __init__(self, name, grade=1):
        self.name = name
        self.grade = grade

s1 = Student("Tom")
print(s1.grade)


class Rectangle:
    def __init__(self, width, height):
        self.area = width * height

r = Rectangle(4, 5)
print(r.area)


class User:
    def __init__(self, age):
        self.is_adult = age >= 18

u = User(20)
print(u.is_adult)
