b = 10  # Global scope variable


def hello():
    x = 2  # local scope variable
    print(b)

    def hi():
        print(x)

    hi()


hello()
print(b)
