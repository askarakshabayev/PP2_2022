# map(func, data)

nums = [48, 6, 9, 21, 1]

square_all = map(lambda num: (num ** 2, num + 2), nums)

print(list(square_all))
