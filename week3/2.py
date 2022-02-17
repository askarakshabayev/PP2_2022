def func(my_list):
    my_list[0] = 'hello'
    my_list[2] = 'world'

    for item in my_list:
        print(item)


l = [1, 2, 10, 20, 30]

func(l)
print(l)
