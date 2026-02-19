def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4))


def print_args(*args):
    for arg in args:
        print(arg)

print_args("apple", "banana", "cherry")


def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)


def combined(a, b, *args, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("kwargs:", kwargs)

combined(1, 2, 3, 4, name="Bob")


def multiply(a, b):
    return a * b

numbers = (3, 5)
print(multiply(*numbers))

