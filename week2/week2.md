# Week2
## Get data from console
#### example 1
```python
s = input()
print(s)
```

#### example 2
```python
a = int(input())
b = int(input())
print(a + b)
```

#### example 3
```python
a, b = input().split()
print(int(a) + int(b))
```

#### example 4
```python
a, b = map(int, input().split()) # '1 2' => ['1', '2'] => [1, 2] => a = 1, b = 2
print(a + b)
```
#### example 5
```python
a = map(int, input().split())
print(a)

for x in a:
    print(x)
```

## Operators example
#### example 6
```python
a = 10
a += 3 # a = a + 3
a <<= 3 # 104
print(a)
print(1 << 10) # 10000000000 => 1024
print(5 >> 1)  # 10 => 2
```

#### example 7
```python
a = 5    # 101
b = 6    # 110
# a ^= b   # 011 => 3 
a &= b # # 100 => 4
print(a)
```

#### example 8
```python
a = 5
b = 6
c = 7
print(not (a > b and a > c)) 
```

## if else
```
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
```
#### example 9
```python
# a, b, c
a, b, c = map(int, input().split())

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)

```

## while loop

#### example 10
```python
i = 0
while i < 6:
    print(i)
    i += 1
    if i == 3:
        break
```

```python
while i < 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)
else:
    print("end")
    

```

#### example 11
```python
a = [12, 3, 8, 10, 13]

for x in a:
    print(x)
```
```python
for x in range(1, 20, 2):
    print(x)
```

#### example 12
```python
a = [1, 2, 3]
b = [3, 4, 5]

for x in a:
    for y in b:
        print(x, y)
```

#### example 13
```python
a = [12, 5, 6, 10]

for i in range(len(a)):
    print(a[i])
```

## list
```
mylist = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]
list4 = ["abc", 34, True, 40, "male"]
```
#### example 14

```python
a = []

for x in range(0, 20, 2):
    a.append(x)

# a.pop(1)
# a.clear()


print(a)
```

#### example 15
```python
a = [1, 2, 3, 1, 2, 3, 1, 2, 3]
a = ["hello", 1, "world", 2, "t", "3", "1", "1"]
x = a.count("1")

print(x)
```

#### example 16
```python
a = [0] * (100)
print(a)
```

#### example 17
```python
a = [1, 2, 3]
b = [5, 6, 7]
a.extend(b)
p = a.index(6)
print(p)
a.insert(1, "hello")
a.remove("hello")
print(a)
```

#### example 18
```python
a = [12, 1, 45, 16, 57]
a.sort()
a.reverse()
print(a)

# a = [[1,2], [3, 4], [5, 6]]
# a[0] = [1, 2]
# a[0][1]
```

```python
a = [1, 2, 3]
# b = a
b = a.copy()

b.append(4)
a.append(5)

print('a =', a)
print('b =', b)


print(hex(id(a)))
print(hex(id(b)))
```

## Tuple
- Tuples are used to store multiple items in a single variable.
- Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.
- A tuple is a collection which is ordered and unchangeable.
- Tuples are written with round brackets.
```python
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
```

## comprehension
#### example 19
```python
# for i in range(5):
#   print(i)

# [print(i) for i in range(5)] # [expression for iter in list condition]


a = [i for i in range(10) if i % 2 != 0]

print(a)
print(type(a))
```
```python
a = [float(n) for n in input('Enter list of numbers...\n').split(' ')]

print([i * 2 for i in a])
print(a)
```

## set
#### example 20
```python
a = {1, 1, 2, 3}
# a = set()

a.add(1)
a.add(1)
a.add(1)
a.add(2)

a.remove(1)

print(len(a))
print(a)
print(type(a))

print(2 in a)

for i in a:
  print(i)

```

#### example
```python
set1 = set()
set1.add(1)
set1.add(2)
set1.add(3)

try:
    set1.remove(10)
except Exception as arg:
    print("Error", str(arg))
print("hello world")
# set1.discard(10)

print(set1)
```
```python
set1 = set([1, 2, 3, 5])
set2 = set([2, 3, 4])
set3 = set([3, 4, 5])
# print(set1.union(set2, set3))
# print(set1.union([10, 11, 12, 11]))
# print(set1.intersection(set2, set3))
# print(set1.difference(set2))
print(set1 - set2 - set3)
```


## dict
#### example 21
```python
# a = {
#   'id': '21B123123',
#   'name': 'Student 1',
#   'age': 18,
#   'gpa': 4.0
# }

a = dict(id='21B123123', name='Student 1', age=18, gpa=4.0)


del a['age']

a.pop('id')

print(len(a))
print(type(a))

print(a.keys())
print(a.values())
print(a.items())

for key, value in a.items():
  print(f'{key} ---> {value}')
```

## random examples
#### example 22
```python
n = int(input())

arr = []
for i in range(n):
  num = [int(n) for n in input().split(' ')]
  arr.append(num)
  

for row in arr:
  print(row)
```