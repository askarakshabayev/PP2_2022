import re
import csv

file = open('raw.data', 'r')
text = file.read()

BINPattern = r'\nБИН.*(?P<BIN>\b[0-9]+)'
NDSPatter = r'\nНДС.*(?P<NDS>\b[0-9]+)'
BINText = re.search(BINPattern, text).group("BIN")
NDSText = re.search(NDSPatter, text).group("NDS")


items = [['БИН', 'НДС', 'Наименование товара', 'Кол-во', 'Цена за единицу']]

itemPatternText = r'(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)'

# itemText = re.search(itemPatternText, text).group('name')
# print(itemText)
itemPattern = re.compile(itemPatternText)

for m in re.finditer(itemPattern, text):
    items.append([BINText, NDSText,m.group('name'), m.group('count'), m.group('price')])

with open('file.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(items)


file.close()