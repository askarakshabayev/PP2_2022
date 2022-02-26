# Week3
## Python Functions
#### example 1
```python
def function_name(arg1, arg2):
    print(arg1 * arg2)

function_name(4, 5)
```

#### example 2
```python
def func(my_list):
    my_list[0] = "Hello"
    my_list[2] = "world"
    # for item in my_list:
    #     print(item)

l = [1, 2, 10, 11, 12]
func(l)
print(l)
```

#### example 3
```python
def func(*args):
    for arg in args:
        print(arg, type(arg))

func([1, 2, 3], "hello", 15)
```
```
def my_sum(*args):
    result = 0
    # Iterating over the Python args tuple
    for x in args:
        result += x
    return result

print(my_sum(1, 2, 3))
```

#### example 4
```python
def f(arg1, arg2, arg3 = "Hello"):
    print(arg1, arg2, arg3)

# f(1, 2)
# f(1, 10, 15)
f(arg2 = 10, arg1 = 15, arg3 = "test")
```
#### example 5
```python
def f(**kwargs):
    print(kwargs["lname"], kwargs["fname"])


f(fname = "Tobias", lname = "Refsnes")
```
#### example 6
```python
def f(a, b, c):
    if (a >= b and a >= c):
        return a
    elif (b >= a and b >= c):
        return b
    return c

m = f(3, 8, 5)
print(m)
```
#### example 7
```python
# a, b
# a * b
# a + b
# a - b

def f(a, b):
    result1 = a * b
    result2 = a + b
    result3 = a - b
    return result1, result2, result3

# a, b, c = f(2, 3)
# print(a, b, c)

# a, _, _ = f(2, 3)
# print(a)

# _, a, _ = f(2, 3)
# print(a)

a, _, b = f(2, 3)
print(a, b)

# print(f(2, 3))
# print(f(2, 3)[1])
```
#### example 8
```python
def rec(n):
    if n == 0 or n == 1:
        return 1
    return rec(n - 1) + rec(n - 2)

print(rec(5))
```

##  Python Lambda
You can write your very own Python functions using the def keyword, function headers, docstrings, and function bodies. However, there's a quicker way to write functions on the fly, and these are called lambda functions because you use the keyword lambda.
#### example
```python
my_power = lambda x, y: x ** y
my_power(2, 3)
```
### map() and lambda Function
The map function takes two arguments, a function and a sequence such as a list and applies the function over all the elements of the sequence. We can pass lambda function to the map without even naming them, and in this case, we refer to them as anonymous functions.
#### example
```python
nums = [48, 6, 9, 21, 1]
square_all = map(lambda num: num ** 2, nums)
print(square_all)
print(list(square_all))
```

```python
def func(n):
    return lambda a: a * n

doubler = func(2) # labmda a: a * 2

print(doubler(3))
print(doubler(6))

triple = func(3) # lambda a: a * 3
print(triple(3))
print(triple(6))

multiple_100 = func(100) # lambda a: a * 100

print(multiple_100(5))
print(multiple_100(6))
```

```python
# only even numbers from a list (using filter)

# def f(x):
#     return x % 2 == 0

# list1 = [2, 3, 5, 8, 16, 100, 103]

# list2 = list(filter(f, list1))

# print(list2)

list1 = [2, 3, 5, 8, 16, 100, 103]
list2 = list(filter(lambda x: x % 2 == 0, list1))
print(list2)
```
```python
# only prime numbers from a list (using filter)

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

list1 = [1, 2, 14, 5, 13, 100, 103]

list2 = list(filter(lambda x: is_prime(x), list1))

print(list2)
```

## Python Classes and Objects
#### example
```python
# class

class MyClass:
    # fields
    x = 5
    y = 6

    # methods
    def sum(self, a, b):
        return self.x + self.y + a + b

a = MyClass() # a.x, a.y
a.x = 10
a.y = 20

b = MyClass() # b.x, b.y
b.x = 7
b.y = 30

print(a.x, a.y)
print(b.x, b.y)
print(a.sum(1, 2)) # 
print(b.sum(3, 4)) # b.x + b.y

```
#### example
```python
class Person:
    
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def show(self):
        print(f'{self.name} - {self.surname}')
        # print("{1} - {0}".format(self.name, self.surname))

    def __str__(self):
        return f'{self.name} - {self.surname}'

a = Person("Askar", "Akshabayev")
b = Person("Aaa", "Bbb")

print(a)
print(b)
```
#### example
```python
class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def show(self):
        print(f'{self.name} - {self.surname}')

class Subject:
    pass


class Student(Person): # Person
    def __init__(self, name, surname, gpa, faculty):
        super().__init__(name, surname) # Person init
        self.gpa = gpa
        self.faculty = faculty

    def show(self):
        super().show()
        print(f'{self.gpa} - {self.faculty}')

a = Student("Aaa", "Bbb", 3.9, "FIT") # a.name, a.surname (Person), a.gpa, a.faculty (Student -> Person)
a.show()
b = Student("Bbb", "Ccc", 4.0, "FOGI")
b.show()

# a = Student("Aaa", "Bbb")
# a.show()
```

