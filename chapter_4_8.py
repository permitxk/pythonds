# -*- coding:utf-8 -*-
from chapter_4_5 import Stack


def devideby2(number):
    s = Stack()
    while number > 0:
        res = number % 2
        number = number // 2
        s.push(res)
    binary_num = ''
    while not s.isEmpty():
        binary_num += str(s.pop())
    return binary_num


print(devideby2(233))
print(devideby2(42))
