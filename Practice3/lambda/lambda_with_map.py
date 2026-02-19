numbers = [1, 2, 3, 4]
squares = list(map(lambda x: x ** 2, numbers))
print(squares)


nums = [1, 2, 3]
strings = list(map(lambda x: str(x), nums))
print(strings)


print(list(map(lambda x: x * 2, numbers)))


words = ["apple", "banana", "cherry"]
print(list(map(lambda w: len(w), words)))


a = [1, 2, 3]
b = [4, 5, 6]
print(list(map(lambda x, y: x + y, a, b)))
