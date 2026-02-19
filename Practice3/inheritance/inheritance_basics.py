class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):
    pass

d = Dog()
d.speak()


class Cat(Animal):
    def meow(self):
        print("Meow")

c = Cat()
c.meow()


print(isinstance(d, Animal))


animals = [Dog(), Cat()]
for animal in animals:
    animal.speak()
