class Person:
    pass


class Car:
    brand = "Toyota"

print(Car.brand)


class Dog:
    species = "Canine"

dog1 = Dog()
print(dog1.species)


dog1.name = "Buddy"
print(dog1.name)


dog2 = Dog()
dog2.name = "Max"
print(dog2.name)
