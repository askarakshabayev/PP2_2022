def f(**kwargs):
    for key in kwargs:
        print(key, kwargs[key])

f(fname = 'Askar', lname = 'Akshabayev')