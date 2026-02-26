def remove_duplicate(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

nums = [1, 2, 3, 2, 4, 1, 5, 3]

# print(remove_duplicate(nums))


list_num = set(nums)
# print(list(list_num))

def sum_of_n(n):
    the_sum = 0
    for i in range(1,n+1):
        the_sum = the_sum + i
    return the_sum

# print(sum_of_n(10))

import time


def sum_of_n_2(n):
    start = time.time()

    the_sum = 0
    for i in range(1, n + 1):
        the_sum = the_sum + i

    end = time.time()

    return the_sum, end - start

for i in range(5):
    print("Sum is %d required %10.7f seconds" % sum_of_n_2(10000))
