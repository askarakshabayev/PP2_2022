import re

file = open('raw.data', 'r')
text = file.read()

itemPatternText = r'(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)'

# itemText = re.search(itemPatternText, text).group('name')
# print(itemText)
itemPattern = re.compile(itemPatternText)

for m in re.finditer(itemPattern, text):
    print(m.group('name') + " " + m.group('count') + " " + m.group('price'))

file.close()