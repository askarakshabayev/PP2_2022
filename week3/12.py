def func(n):
    return lambda a: a * n


# doubler = func(2)  # lambda a: a * 2
#
# print(doubler(3))
# print(doubler(6))

# triple = func(3)
# print(triple(3))
# print(triple(6))

multiple_100 = func(100)  # lambda a: a * 100

print(multiple_100(3))