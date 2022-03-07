import re

pattern = r'\b\w{3}\b'
text = 'abc defpppp k12 lll$    fff mmm'

print(re.findall(pattern, text))

