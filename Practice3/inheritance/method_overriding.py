class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    def speak(self):
        print("Bark")

d = Dog()
d.speak()


class Cat(Animal):
    def speak(self):
        print("Meow")

c = Cat()
c.speak()


class Parrot(Animal):
    def speak(self):
        super().speak()
        print("Squawk")

p = Parrot()
p.speak()


animals = [Dog(), Cat(), Parrot()]
for animal in animals:
    animal.speak()
