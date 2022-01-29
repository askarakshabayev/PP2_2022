# a = "abc,def,qwe"
#
# print(a.split(','))

# a = "abc, def, klm"
# print(a.split(', '))

# a = "abc:def:klm"
# print(a.split(':'))
#
# b = a.split(":")
#
# print(b[1])

txt = """line1 text
line2 text1 text2 text3
line3 text"""

a = txt.split('\n')

print(a[1].split(' '))

