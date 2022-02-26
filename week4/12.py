import json

f = open('input.txt', 'r')
text = f.read()
teacher = json.loads(text)

print(teacher['name'], teacher['surname'])