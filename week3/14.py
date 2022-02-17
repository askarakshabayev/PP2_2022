def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

list1 = [1, 2, 14, 5, 13, 100, 103]

list2 = list(filter(lambda x: is_prime(x), list1))

print(list2)