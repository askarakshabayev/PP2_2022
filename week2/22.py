a = [1, 2, 3]
b = a.copy()

a.append(4)
b.append(5)

print(a)
print(b)

print(hex(id(a)))
print(hex(id(b)))