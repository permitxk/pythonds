# -*- coding:utf-8 -*-
import timeit
import time
import random
for i in range(10000, 100001, 20000):
    t = timeit.Timer("random.randrange(%d) in x" % i, "from __main__ import random, x")
    x = list(range(i))
    lst_time = t.timeit(number=1000)
    x = {j: None for j in range(i)}
    d_time = t.timeit(number=1000)
    print("%d,%10.3f,%10.3f" % (i, lst_time, d_time))


for i in range(10000, 100001, 20000):
    index = random.randrange(i)
    t = timeit.Timer("x[index]", "from __main__ import x, index")
    x = list(range(i))
    res_time = t.timeit(number=1000)
    print(i, res_time)

for i in range(10000, 100001, 20000):
    t1 = timeit.Timer("del x[random.randrange(i-1000)]", "from __main__ import random, i, x")
    x = list(range(i))
    list_time = t1.timeit(number=1000)
    x = {j: None for j in range(i)}
    start_time = time.time()
    for k in range(1000):
        del x[k]
    end_time = time.time()
    dict_time = end_time - start_time
    print(i, list_time, dict_time)


def partition(list, left, right):
    base = list[left]
    while left < right:
        while list[right] >= base and left < right:
            right -= 1
        list[left] = list[right]
        while list[left] <= base and left < right:
            left += 1
        list[right] = list[left]
    list[right] = base
    return left


def quick_sort(list, left, right):
    """
    修改不同的left和right，可以通过递归将list不同位置的顺序调顺
    :param list:
    :param left:
    :param right:
    :return:
    """
    if left < right:
        temp = partition(list, left, right)
        quick_sort(list, left, temp - 1)
        quick_sort(list, temp + 1, right)
    return list


def q_sort(list):
    left = 0
    right = len(list) - 1
    return quick_sort(list, left, right)


test = [2, 4, 5, 1, 1, 3]
print(quick_sort(test, 0, len(test) - 1))
print(test)


def find_k_small(list, k):
    if k > len(list):
        return "out of range!"
    else:
        list_sorted = q_sort(list)
        return list_sorted[k - 1]


print(find_k_small(test, 3))
