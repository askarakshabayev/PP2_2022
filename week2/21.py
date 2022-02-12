a = [1, 2, 3]  # a -> 123
b = a          # b -> 123
a.append(4)
b.append(5)

print(hex(id(a)))
print(hex(id(b)))
