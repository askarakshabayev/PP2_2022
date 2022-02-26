def fib(n):
    a, b = 0, 1  # a = 0, b = 1
    for _ in range(n):
        yield a  # 1
        a, b = b, a + b  # a = 1, b = 2


a = fib(20)

b = list(a)

print(b)

