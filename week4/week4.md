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

## Regex
Регулярка	Её смысл
- simple text	---  В точности текст «simple text»
- \d{5}	--- Последовательности из 5 цифр, \d означает любую цифру, {5} — ровно 5 раз
- \d\d/\d\d/\d{4} -	Даты в формате ДД/ММ/ГГГГ (и прочие куски, на них похожие, например, 98/76/5432)
- \b\w{3}\b	- Слова в точности из трёх букв, \b означает границу слова, (с одной стороны буква, а с другой — нет), \w — любая буква, {3} — ровно три раза
- [-+]?\d+	Целое число, например, 7, +17, -42, 0013 (возможны ведущие нули), [-+]? — либо -, либо +, либо пусто, \d+ — последовательность из 1 или более цифр

## Functions
- re.search(pattern, string) - Найти в строке string первую строчку, подходящую под шаблон pattern;
- re.fullmatch(pattern, string) - Проверить, подходит ли строка string под шаблон pattern;
- re.split(pattern, string, maxsplit=0) - Аналог str.split(), только разделение происходит по подстрокам, подходящим под шаблон pattern;
- re.findall(pattern, string) - Найти в строке string все непересекающиеся шаблоны pattern;
- re.finditer(pattern, string) - Итератор всем непересекающимся шаблонам pattern в строке string (выдаются match-объекты);
- re.sub(pattern, repl, string, count=0) - Заменить в строке string все непересекающиеся шаблоны pattern на repl;

```python
# RegEx - Regular Expression
import re


txt = "The          rain     in      Spain"
x = re.split("in", txt)
x = re.split(" ", txt)
x = re.split("\s+", txt)
x = re.split("\s+", txt, 2)

print(x)
```

```python
import re 

match = re.search(r'\d\d\D\d\d', r'Телефон 123-12-12') 
print(match[0] if match else 'Not found') 
# -> 23-12 
match = re.search(r'\d\d\D\d\d', r'Телефон 1231212') 
print(match[0] if match else 'Not found') 
# -> Not found 

match = re.fullmatch(r'\d\d\D\d\d', r'12-12') 
print('YES' if match else 'NO') 
# -> YES 
match = re.fullmatch(r'\d\d\D\d\d', r'Т. 12-12') 
print('YES' if match else 'NO') 
# -> NO 

print(re.split(r'\W+', 'Где, скажите мне, мои очки??!')) 
# -> ['Где', 'скажите', 'мне', 'мои', 'очки', ''] 

print(re.findall(r'\d\d\.\d\d\.\d{4}', 
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# -> ['19.01.2018', '01.09.2017'] 

for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'): 
    print('Дата', m[0], 'начинается с позиции', m.start()) 
# -> Дата 19.01.2018 начинается с позиции 20 
# -> Дата 01.09.2017 начинается с позиции 45 

print(re.sub(r'\d\d\.\d\d\.\d{4}', 
             r'DD.MM.YYYY', 
             r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# -> Эта строка написана DD.MM.YYYY, а могла бы и DD.MM.YYYY 

```

```python
txt = '''asd@gmail.com
Asd2213@mail.ru
asd3_asd@gmail.com
bobur.mukhsimbaev@kbtU.kz
aSd21as..das.@kbtu.kz
asd21as..das@-k.kz
asd21as..das@.k.kz123
asd21as..dask.kz123


20.02.2021  14:56:10
20.02.21  14:56::10
203.022.2021  14d2:56:10d
.022.2021  142:56.:10d

+7707-123-11-22
+7(707)123-11-22
8(707)123-11-22
707-12-11.222
70-123-11-22


22
,724
,900

Kazakhstan,[apple] officially the Republic of Kazakhstan,[four][4][13123] is a transcontinental country mainly.
located in Central Asia with a smaller portion west of the Ural River in Eastern Europe. It covers a 
land area of 22,724,900 square kilometres (110,052,100 sq mi), and shares land borders with Russia in the 
north, China in the east, and Kyrgyzstan, Uzbekistan, and Turkmenistan in the south while also adjoining 
a large part of the Caspian Sea in the southwest. Kazakhstan does not border Mongolia, although they are 
only 37 kilometers apart.

Kazakhstan is the world's largest landlocked country, and the ninth-largest country in the world. It has 
a population of 18.81131 million residents, 18.81 and has one of the lowest population densities in the world, at 
fewer than 6 people per square kilometre (15 people per sq mi). Since 1997, the capital is Nur-Sultan, 
formerly known as Astana. It was moved from Almaty, the country's largest city.'''



import re

'''
# Examples from text:
  - \w+stan ----> Kazakhstan   ---  Kyrgyzstan  ---- Uzbekistan
  - \d{2}\.\d{2}\.\d{2,4} ----> Selecting Date with format:  20.02.2021 
  - \d{2}:\d{2}:\d{2} ----->  Selecting time with format: 14:56:10
  - (\+7|8)\(?\d{3}\)?-?\d{3}-\d{2}-\d{2} ---> +7707-123-11-22  ----- +7(707)123-11-22 ---- 8(707)123-11-22
  - [a-z]+@[a-z]+\.[a-z]{2,5}   --->   asd@gmail.com
  - [a-z0-9_]+@[a-z]+\.[a-z]{2,5} --->  asd3_asd@gmail.com
  - [A-Za-z0-9_]+\.?[A-Za-z0-9_]+@[a-z]+\.[a-z]{2,4}  --->  bobur.mukhsimbaev@kbtu.kz
  - [\w]+\.?[\w]+@[\w]+\.[\w]{2,4}  ---> askar.akshabayev@kbtu.kz
  - \[\w+\] ---> [apple],[four],[4],[13123]
  - \d+(,\d{3})+ --->  22,724,900     ----     110,052,100
  - \d+\.\d{1,}  ---> 18.81131
'''

# [A-Za-z0-9_]  <==> \w
# \d{1,}   <==> \d+
# \d{0,}   <==> \d*
# \d{0,1}   <==> \d?


email_pattern = re.findall(r'[\w]+\.?[\w]+@[\w]+\.[\w]{2,4}', txt)


```