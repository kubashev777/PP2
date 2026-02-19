def introduce(name, age):
    print(f"My name is {name}, I am {age} years old.")

introduce("Bob", 25)

introduce(age=30, name="Anna")


def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()
greet("Tom")


def power(base, exponent=2):
    print(base ** exponent)

power(4)
power(2, 3)


def describe_pet(pet_name, animal_type="dog"):
    print(f"I have a {animal_type} named {pet_name}.")

describe_pet("Buddy")
describe_pet("Murka", "cat")
