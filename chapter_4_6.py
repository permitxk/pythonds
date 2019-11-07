# -*- coding:utf-8 -*-
from chapter_4_5 import Stack


def parChecher(symbolString):
    a = [")", "]", "}"]
    b = ["()", "[]", "{}"]
    right_set = set(a)
    correct_set = set(b)
    s = Stack()
    is_balance = True
    if len(symbolString) == 0:
        return is_balance
    else:
        for j in symbolString:
            if j == ' ':
                continue
            else:
                if (j in right_set) and s.size() >= 1:
                    if s.peek() + j in correct_set:
                        s.pop()
                    else:
                        s.push(j)
                else:
                    s.push(j)
        if s.size() != 0:
            is_balance = False
    return is_balance


print(parChecher('{ { ( [ ] [ ] ) } ( ) }'))
print(parChecher('[ [ { { ( ( ) ) } } ] ]'))
print(parChecher('[{()]'))


