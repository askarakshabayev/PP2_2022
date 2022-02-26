#  JSON - JavaScript Object Notation

import json

a = {
    'id': '20BD1212',
    'name': 'Student 1',
    'age': 20
}

b = json.dumps(a)

c = json.loads(b)

print(c['id'])
print(c['name'])
print(c['age'])

print(a == c)
