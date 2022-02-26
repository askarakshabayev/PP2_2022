# simple text  - в точности 'simple text'
# \d{5} - последовательность из 5 цифр
# \d\d/\d\d/\d\{4} - DD/MM/YYYY
# \b\w{3}\b

import re

match = re.findall(r'\d\d\D\d\d', r'Phone 123-12-12')

print(match[0] if match else 'Not found')

