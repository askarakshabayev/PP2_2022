## Topics covered in this lab work
- Python Iterators, Generators
- Python Scope
- Python Modules
- Python Dates
- Python Math
- Python JSON
- RegEx

## Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

#### example
```python
list1 = [10, 5, 23, 6, 12]

# for item in list1:
#     print(item)

# __iter__
# __next__

it = iter(list1)

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

```
#### example
```python
class MyNumber:
    def __iter__(self):
        self.x = 1
        return self
    
    def __next__(self):
        x = self.x
        self.x += 1
        return x

a = MyNumber()

# it = iter(a) # __iter__ x = 1

# print(next(it)) # __next__ 
# print(next(it)) # __next__
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for item in a:
    print(item) 
```
#### example
```python
class Fib:
    def __init__(self, limit):
        self.limit = limit

    def __iter__(self):
        self.x = 0
        self.y = 1
        self.cnt = 1
        return self

    def __next__(self): # 3 5
        if self.cnt > self.limit:
            raise StopIteration

        x, y = self.x, self.y
        self.x, self.y = self.y, self.x + self.y
        self.cnt += 1
        return x + y

a = Fib(10)
# it = iter(a)

# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))

for i in a:
    print(i)
```

### Generator
The difference is that while a return statement terminates a function entirely, yield statement pauses the function saving all its states and later continues from there on successive calls.
#### example
```python
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n
    n += 1
    print('This is printed second')
    yield n
    n += 1
    print('This is printed at last')
    yield n
    
a = my_gen()
next(a)
next(a)
next(a)

for item in my_gen():
    print(item)
```
#### example
```python
a = int(input('Give amount: '))

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# print(list(fib(a)))
a = fib(10)
next(a)
next(a)
```

## Scope
#### example
```python
b = 10 # Global scope variable

def hello():
  x = 2  # Local scope variable
  print(b)
  def hi():
    print(x)
  hi()

# print(x) # x is not defined here

hello()
print(b)

```
#### example
```python
def hello():
  global x
  x = 20

hello()

print(x)
```
#### example
mymodule.py
```python
def hello():
  print('hi')

def hello2():
  print('hello 2')
x = 20
```
```python
import mymodule
from mymodule import hello2
from mymodule import hello as hi

mymodule.hello()
print(mymodule.x)

hello2()
hi()

```
## Datetime
#### example
```python
from datetime import datetime

now = datetime.now()

print(now)
print(now.day)
print(now.year)
print(now.month)
print(now.strftime("%m:%Y"))

now = datetime(2018, 3, 15)

print(now.strftime("%A"))
print(now.strftime('%d/%m/%Y %H:%M:%S'))
```
## math
#### example
```python
import math

a = min(1, 2, 4, 5)
b = max(1, 2, 4, 5)
print(a, b)

a = pow(2, 3)
print(a)

a = abs(-3)
print(a)


print(math.sqrt(9))
print(math.floor(2.7))
print(math.ceil(2.001))
print(round(2.4))
```
## json
#### example
```python
# JSON -> JavaScript Object Notation
import json

a = {
  'id': '20BD1212',
  'name': 'Student 1',
  'age': 20
}
b = json.dumps(a) # serializing dict to str

print(type(b))
print(b)

c = json.loads(b)  # deserializing str back to dicts
print(a == c)
print(type(c))
print(c['age'])
print(c['name'])
```
#### example
input.txt
``` 
{"name": "Askar", "surname": "Akshabayev", "ID": 13}
```
```python
import json

f = open("input.txt", "r")
text = f.read()
teacher = json.loads(text)
print(teacher['name'], teacher['ID'])
```
```python
import json
game_state = {
    "position": {
        "x": 100,
        "y": 200
    }
}

game_state["full_name"] = "Hello world"
game_state["enemy"] = {
    "x": 200,
    "y": 300
}

f = open("output.txt", "w")
f.write(json.dumps(game_state))
f.close()
```
