class Fib:

    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 0
        self.y = 1
        self.cnt = 1
        return self

    def __next__(self):
        if self.cnt > self.limit:
            raise StopIteration

        x, y = self.x, self.y
        self.x, self.y = self.y, self.x + self.y
        self.cnt += 1
        return x + y


# a = Fib(10)

# it = iter(a)
#
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

fib_numbers = Fib(10)

for item in fib_numbers:
    print(item)
