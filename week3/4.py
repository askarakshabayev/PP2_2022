def my_sum(*args):
    result = 0
    for x in args:
        result += x
    return result

sum1 = my_sum(1, 2, 3, 4, 5)
sum2 = my_sum(1, 2, 3)
print(sum1)
print(sum2)