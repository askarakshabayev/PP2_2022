# 12-56
import re

# Search example
# match = re.search(r'\d\d\D\d\d', r'phone 123-12-12')
# match = re.search(r'\d\d\D\d\d', r'phone 1231212')
#
# print(match[0] if match else 'Not found')

match = re.fullmatch(r'\d\d\D\d\d', r'phone 12-12')
print('YES' if match else "NO")
