nums = [5, 2, 9, 1]
print(sorted(nums, key=lambda x: x))


words = ["apple", "kiwi", "banana"]
print(sorted(words, key=lambda w: len(w)))


pairs = [(1, 3), (2, 1), (4, 2)]
print(sorted(pairs, key=lambda x: x[1]))


print(sorted(nums, key=lambda x: x, reverse=True))


print(sorted(words, key=lambda w: w[-1]))
