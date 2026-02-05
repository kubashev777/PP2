#1
for i in range(5):
    if i == 3:
        continue
    print(i)

#2
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)

#3
for num in range(10):
    if num % 2 == 0:
        continue
    print(num)

#4
names = ["Alice", "Bob", "Charlie"]
for name in names:
    if name.startswith("B"):
        continue
    print(name)

#5
for i in range(1, 6):
    if i == 4:
        continue
    print(i)