#  *args
def func(a, *args):  # args = [[1, 2, 3[, "hello", 10]
    for arg in args:
        print(arg, type(arg))

func([1, 2, 3], "hello", 10)
func(1, 2, 3, 4, 5)
