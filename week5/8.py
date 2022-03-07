import re

print(re.sub(r'\d\d.\d\d.\d{4}', 'DD/MM/YYYY', 'test 19.01.2018 as;dlkfjasldjf;alskj 01.09.2017'))