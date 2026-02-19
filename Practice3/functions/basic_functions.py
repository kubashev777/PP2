def greet():
    print("Hello, world!")

greet()


def greet_name(name):
    print(f"Hello, {name}!")

greet_name("Alice")


def add(a, b):
    print(a + b)

add(5, 3)


def is_even(number):
    if number % 2 == 0:
        print("Even")
    else:
        print("Odd")

is_even(10)


def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)
