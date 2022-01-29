a = "hello"


def func():
    global a
    a = "abc"
    print("hi" + a)


func()
print(a)