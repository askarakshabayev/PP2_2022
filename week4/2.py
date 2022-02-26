class MyNumber:
    def __iter__(self):
        self.x = 1
        return self

    def __next__(self):
        x = self.x
        self.x += 1
        return x


a = MyNumber()

# it = iter(a)
#
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for item in a:
    print(item)
