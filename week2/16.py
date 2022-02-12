a = []

for x in range(0, 20, 2):
    a.append(x)

a.pop(1)
a.pop(5)

a.clear()
print(a)