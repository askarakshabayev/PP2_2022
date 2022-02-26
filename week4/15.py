import re

# print(re.split(r'\W+', 'Hello,    world,   my  name is Askar!!!'))
# print(re.split(r'\w+', 'Hello,    world,   my  name is Askar!!!'))

print(re.findall(r'\d\d.\d\d.\d{4}', 'asdf 19.01.2018  bbbb  01.02.2022'))