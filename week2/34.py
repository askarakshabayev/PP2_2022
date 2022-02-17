# 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4
# 1 2 3 4

n = int(input())

arr = []

for i in range(n):
    nums = [int(n) for n in input().split(' ')]
    arr.append(nums)

for row in arr:
    print(row)

# print(arr)