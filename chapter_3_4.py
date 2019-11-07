# -*-coding:utf-8 -*-
def anagram_find_1(s1, s2):
    stillok = True
    if len(s1) != len(s2):
        stillok = False
    alist = list(s2)
    pos1 = 0
    while pos1 < len(s1) and stillok:
        pos2 = 0
        found = False
        while pos2 < len(alist) and not found:
            if s1[pos1] == alist[pos2]:
                found = True
                alist[pos2] = None
            else:
                pos2 += 1
        if not found:
            stillok = False
        pos1 = pos1 + 1
    return stillok


print(anagram_find_1('abfddcd', 'dcbaddf'))


def anagram_find_2(s1, s2):
    still_ok = True
    if len(s1) != len(s2):
        still_ok = False
    a_list = list(s2)
    for i in range(len(s1)):
        for j in range(len(a_list)):
            if s1[i] == a_list[j]:
                a_list[j] = None
                break
            else:
                if j == len(a_list)-1:
                    still_ok = False
                    return still_ok
    return still_ok


print(anagram_find_2('abfddcd', 'dcbaddf'))


def anagram_find_3(s1, s2):
    new_s1 = list(s1)
    new_s2 = list(s2)
    new_s1.sort()
    new_s2.sort()
    i = 0
    still_ok = True
    while i < len(new_s1) and still_ok:
        if new_s1[i] != new_s2[i]:
            still_ok = False
        i += 1
    return still_ok


print(anagram_find_3('abfddcd', 'dcbaddf'))


def anagram_find_4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in s1:
        num1 = ord(i) - ord('a')
        c1[num1] += 1

    for j in s2:
        num2 = ord(j) - ord('a')
        c2[num2] += 1

    still_ok = True
    index = 0
    while index < 26 and still_ok:
        if c1[index] != c2[index]:
            still_ok = False
        else:
            index += 1
    return still_ok


print(anagram_find_4('abfddcd', 'dcbaddf'))
