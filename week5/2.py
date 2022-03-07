import re
# DD/MM/YYYY

pattern = r'\d\d/\d\d/\d{4}'
text = '12/01/1989 test ppp 13/02/1986    45/56/9000'

print(re.findall(pattern, text))

