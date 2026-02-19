class Animal:
    def __init__(self, name):
        self.name = name


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

d = Dog("Buddy", "Labrador")
print(d.name, d.breed)


class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow")

c = Cat("Murka")
c.speak()


class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

b = Bird("Parrot", True)
print(b.can_fly)


class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed)

p = Puppy("Max", "Beagle")
print(p.name)
