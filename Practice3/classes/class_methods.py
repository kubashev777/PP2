class Person:
    def greet(self):
        print("Hello!")

p = Person()
p.greet()


class Calculator:
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(2, 3))


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

c = Counter()
c.increment()
print(c.count)


class Circle:
    def area(self, radius):
        return 3.14 * radius ** 2

circle = Circle()
print(circle.area(3))


class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

acc = BankAccount(100)
acc.deposit(50)
print(acc.get_balance())
