numbers = [1, 2, 3, 4, 5, 6]
print(list(filter(lambda x: x % 2 == 0, numbers)))


nums = [-2, -1, 0, 1, 2]
print(list(filter(lambda x: x > 0, nums)))


words = ["hi", "hello", "cat", "banana"]
print(list(filter(lambda w: len(w) > 3, words)))


print(list(filter(lambda x: x % 2 != 0, numbers)))


nums2 = [5, 12, 17, 3, 9]
print(list(filter(lambda x: x > 10, nums2)))
