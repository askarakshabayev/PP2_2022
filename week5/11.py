import re

file = open('raw.data', 'r')
text = file.read()

BINPattern = r'\nБИН.*(?P<BIN>\b[0-9]+)'
NDSPatter = r'\nНДС.*(?P<NDS>\b[0-9]+)'
BINText = re.search(BINPattern, text)
NDSText = re.search(NDSPatter, text)

print(BINText.group('BIN'))
print(NDSText.group('NDS'))

file.close()