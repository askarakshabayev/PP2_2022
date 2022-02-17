result = dict()


def rec(n):
    if n in result:
        return result[n]

    if n == 0 or n == 1:
        return 1
    result[n] = rec(n - 1) + rec(n - 2)
    return result[n]

print(rec(5))