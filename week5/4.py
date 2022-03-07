import re

text = '7 test +17 ppp -67123 00123'
pattern = r'[+-]?\d+'

print(re.findall(pattern, text))

# re.search(pattern, text)
# re.fullmatch(pattern, text) - проверку что строка text подходит под pattern
# re.split(pattern, text)
# re.findall(pattern, text)
# re.finditer(pattern, text)
# re.sub(pattern, repl, text)



