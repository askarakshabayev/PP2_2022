a, b, c = map(int, input().split())

# a == b
# a != b
# a < b
# a <= b
# a > b
# a >= b
# and or not is

if a >= b and a >= c:
    print(a)
elif b >= a and b >= c:
    print(b)
else:
    print(c)
