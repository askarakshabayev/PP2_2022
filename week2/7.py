a = 5  # 101
b = 3  # 011
       # 011 => 3
# a ^= b
a &= b

# 1 & 1 = 1
# 1 & 0 = 0
# 0 & 1 = 0
# 0 & 0 = 0

# 5 = 101
# 6 = 110
#     100 => 4

print(a)

