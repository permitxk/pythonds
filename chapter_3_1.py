# -*- coding:utf-8 -*-
import time


def sum_of_n2(n):
    start = time.time()
    s = 0
    for i in range(n+1):
        s += i
    end = time.time()
    return s, end - start


for i in range(5):
    print("Sum is %d, and required %10.7f seconds" % sum_of_n2(100000))


def sum_of_n3(n):
    start = time.time()
    s = (1+n) * n / 2
    end = time.time()
    return s, end - start


print('\n')
for i in range(5):
    print("Sum is %d, and required %10.7f seconds" % sum_of_n3(100000))
