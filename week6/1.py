f = open('input.txt', 'r')  # open(path, mode) - mode = 'r', 'w', 'a', 'x'
# print(f)
# print(f.read())
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()
# line5 = f.readline()
#
# print(line1, line2, line3, line4, line5)

# lines = f.readlines()
# print(lines)

for line in f:
    print(line)

f.close()