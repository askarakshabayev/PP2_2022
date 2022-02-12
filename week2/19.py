# d = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]

# d = []
# a = [1, 2, 3]  # list(map(int, input().split()))
# b = [4, 5, 6]
# c = [7, 8, 9]
# d.append(a)
# d.append(b)
# d.append(c)

a = [1, 2, 3]
b = [5, 6, 7]

# c = [a[i] + b[i] for i in range(len(a))]

a.extend(b)

# p = a.index(6)
# print(p)

a.insert(1, "hello")
a.insert(4, "hello")
a.remove("hello")

print(a)