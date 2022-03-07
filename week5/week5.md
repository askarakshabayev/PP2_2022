## Regex
Регулярка	Её смысл
- \d{5}	--- Последовательности из 5 цифр, \d означает любую цифру, {5} — ровно 5 раз
- \d\d/\d\d/\d{4} -	Даты в формате ДД/ММ/ГГГГ (и прочие куски, на них похожие, например, 98/76/5432)
- \b\w{3}\b	- Слова в точности из трёх букв, \b означает границу слова, (с одной стороны буква, а с другой — нет), \w — любая буква, {3} — ровно три раза
- [-+]?\d+	Целое число, например, 7, +17, -42, 0013 (возможны ведущие нули), [-+]? — либо -, либо +, либо пусто, \d+ — последовательность из 1 или более цифр

## Functions
- re.search(pattern, string) - Найти в строке string первую строчку, подходящую под шаблон pattern;
- re.fullmatch(pattern, string) - Проверить, подходит ли строка string под шаблон pattern;
- re.split(pattern, string) - Аналог str.split(), только разделение происходит по подстрокам, подходящим под шаблон pattern;
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

print(x)
```

```python
import re 
# 12-12 
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


# Split по не символам
print(re.split(r'\W+', 'Где, скажите мне, мои очки??!')) 
# -> ['Где', 'скажите', 'мне', 'мои', 'очки', ''] 


# Найти все года
print(re.findall(r'\d\d\.\d\d\.\d{4}', 
                 r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017')) 
# -> ['19.01.2018', '01.09.2017'] 

# Найти позицию каждого вхождения 
for m in re.finditer(r'\d\d\.\d\d\.\d{4}', r'Эта строка написана 19.01.2018, а могла бы и 01.09.2017'): 
    print('Дата', m[0], 'начинается с позиции', m.start()) 
# -> Дата 19.01.2018 начинается с позиции 20 
# -> Дата 01.09.2017 начинается с позиции 45 

# Сделать замену даты на 'DD.MM.YYYY'
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
  - [a-z]+@[a-z]+\.[a-z]{2,5}   --->   asd@gmail.com (only symbols)
  - [a-z0-9_]+@[a-z]+\.[a-z]{2,5} --->  asd3_asd@gmail.com
  - [A-Za-z0-9_]+\.?[A-Za-z0-9_]+@[a-z]+\.[a-z]{2,4}  --->  bobur.mukhsimbaev@kbtu.kz
  - [\w]+\.?[\w]+@[\w]+\.[\w]{2,4}  ---> askar.akshabayev@kbtu.kz
  - \[\w+\] ---> [apple],[four],[4],[13123]
  - \d+[,\d{3}]+ --->  сумма через запятую 22,724,900     ----     110,052,100
  - \d+\.\d{1,}  ---> 18.81131
'''

# [A-Za-z0-9_]  <==> \w
# \d{1,}   <==> \d+
# \d{0,}   <==> \d*
# \d{0,1}   <==> \d?


```
## Groups
```python
import re
txt = 'The rain in Spain 1234'

# x = re.search(r'[0-9]+', txt)
# x = re.search(r'([0-9]+)', txt)
# x = re.search(r'(.+)([0-9]+)', txt)
# x = re.search(r'(.+)(\b[0-9]+)', txt)
x = re.search(r'(?P<text>.+)(?\P<number>\b[0-9]+)', txt)

print(x.groups())
print(x.groups(0))
print(x.group('text'))

```


```python

# Find bin and nds
import re

file = open('raw.data','r')
text = file.read()

BINPattern = r'\nБИН.*'
# BINPattern = r'\nБИН(.*)'
# BINPattern = r'\nБИН([0-9]*)' wrong
# BINPattern = r'\nБИН.*(\b[0-9]+)'
# BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
# NDSPattern = r"\nНДС.*(?P<NDS>\b[0-9]+)"

BINText = re.search(BINPattern, text).group("BIN")
# NDSText = re.search(NDSPattern, text).group("NDS")

# print(NDSText)
print(BINText.group(1))

file.close()
```

```python

import re

file = open('raw.data','r')
text = file.read()

pattern = r"\nБИН.*(?P<BIN>\b[0-9]+).*\nНДС.*(?P<NDS>\b[0-9]+)"

x = re.compile(pattern)

for match in x.finditer(text):
    print(match)
```

```python
import re

file = open('raw.data','r')
text = file.read()

itemPatternText = r"(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemText = re.search(itemPatternText, text).group('total1')

print(itemText)

# itemPatternText = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
# itemPattern = re.compile(itemPatternText)


# for m in re.finditer(itemPattern, text):
#     print(m.group("name") + " " + m.group("count") + m.group("price"))


file.close()
```

```python
import re
import csv

file = open('raw.data','r')
text = file.read()


BINPattern = r"\nБИН.*(?P<BIN>\b[0-9]+)"
NDSPattern = r"\nНДС.*(?P<NDS>\b[0-9]+)"

BINText = re.search(BINPattern, text).group("BIN")
NDSText = re.search(NDSPattern, text).group("NDS")


itemPatternText = r"(?P<name>.*)\n{1}(?P<count>.*)x(?P<price>.*)\n{1}(?P<total1>.*)\n{1}Стоимость\n{1}(?P<total2>.*)"
itemPattern = re.compile(itemPatternText)


items = [["БИН","НДС","Наименование товара","Кол-во","Цена за единиц"]]

for m in re.finditer(itemPattern, text):
    items.append([BINText,NDSText, m.group("name").strip(),m.group("count").strip(), m.group("price").strip()])

with open('file.csv','w',newline='') as f:
    writer = csv.writer(f)
    writer.writerows(items)

file.close()
```

