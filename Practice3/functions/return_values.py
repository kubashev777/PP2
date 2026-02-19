def square(x):
    return x * x

result = square(4)
print(result)


def full_name(first, last):
    return f"{first} {last}"

print(full_name("John", "Doe"))


def min_max(numbers):
    return min(numbers), max(numbers)

print(min_max([1, 5, 3, 9]))


def is_positive(number):
    return number > 0

print(is_positive(-5))


def check_age(age):
    if age < 18:
        return "Underage"
    return "Adult"

print(check_age(20))
