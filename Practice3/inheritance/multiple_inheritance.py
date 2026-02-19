class Flyer:
    def fly(self):
        print("Flying")


class Swimmer:
    def swim(self):
        print("Swimming")


class Duck(Flyer, Swimmer):
    pass

d = Duck()
d.fly()
d.swim()


print(isinstance(d, Flyer))


class SuperDuck(Duck):
    def fly(self):
        print("Super flying")

sd = SuperDuck()
sd.fly()
