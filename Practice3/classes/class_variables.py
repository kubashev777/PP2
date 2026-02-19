class Person:
    species = "Human"

print(Person.species)


p = Person()
print(p.species)


Person.species = "Homo sapiens"
print(p.species)


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
print(Counter.count)


class Car:
    wheels = 4

    def __init__(self, brand):
        self.brand = brand

car1 = Car("Toyota")
print(car1.wheels)
