def my_gen():
    n = 1
    print('first time printing')
    yield n

    n += 1
    print('second time printing')
    yield n

    n += 1
    print('end')
    yield n


# a = my_gen()
#
# next(a)
# next(a)
# next(a)
# next(a)

for item in my_gen():
    print(item)
