set1 = set([1, 2, 3, 5])
set2 = set([2, 3, 4])
set3 = set([3, 4, 5, 6])

# print(set1.union(set2, set3))
# print(set1.union([10, 20, 1, 2]))
# print(set1.intersection(set2, set2))
# print(set1.difference(set2))
print(set1 - set2 - set3)