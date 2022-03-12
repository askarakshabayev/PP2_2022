import re
import os
text = 'test 19.01.2018 as;dlkfjasldjf;alskj 01.09.2017'

for m in re.finditer(r'\d\d.\d\d.\d{4}', text):
    print('Дата', m[0], 'начинается с позиции', m.start())


text = 'print(100)\nprint(200)'
x = compile(text, 'test', 'exec')
exec(x)