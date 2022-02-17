a = ['hello', 'world', 'abc', 'hello', 'world', 'hello']

d = dict()

for s in a:
    if s not in d:
        d[s] = 0
    d[s] += 1

for key in d:
    print(key, d[key])

# d.pop('hello')
# print(d)

# print(d.keys())
# print(d.values())
# print(d.items())

for key, value in d.items():
    print(f'{key} ---> {value}')
