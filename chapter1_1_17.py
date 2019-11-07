# -*- coding: utf-8 -*-
def gcd(m, n):
    while (n != 0) and (m % n != 0):
        oldm = m
        oldn = n
        m = oldn
        n = oldm % oldn
    return n


class Fraction:
    def __init__(self, top, button):
        self.num = top
        self.den = button

    def __str__(self):
        return str(self.num) + '/' + str(self.den)

    def __add__(self, other):
        newnum = self.num*other.den + self.den*other.num
        newden = self.den * other.den
        factor = gcd(newnum, newden)
        return Fraction(int(newnum/factor), int(newden/factor))

    def __sub__(self, other):
        newnum = self.num*other.den - self.den*other.num
        newden = self.den * other.den
        factor = gcd(newnum, newden)
        return Fraction(int(newnum/factor), int(newden/factor))

    def __mul__(self, other):
        newnum = self.num * other.num
        newden = self.den * other.den
        factor = gcd(newnum, newden)
        return Fraction(int(newnum/factor), int(newden/factor))

    def __truediv__(self, other):
        newnum = self.num * other.den
        newden = self.den * other.num
        factor = gcd(newnum, newden)
        return Fraction(int(newnum/factor), int(newden/factor))

    def __gt__(self, other):
        a = self.num / self.den
        b = other.num / other.den
        return a > b

    def __ge__(self, other):
        a = self.num / self.den
        b = other.num / other.den
        return a >= b

    def __lt__(self, other):
        a = self.num / self.den
        b = other.num / other.den
        return a < b

    def __le__(self, other):
        a = self.num / self.den
        b = other.num / other.den
        return a <= b

    def __ne__(self, other):
        a = self.num / self.den
        b = other.num / other.den
        return a != b

    def __radd__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        factor = gcd(newnum, newden)
        return Fraction(int(newnum / factor), int(newden / factor))

    def __iadd__(self, other):
        newnum = self.num * other.den + self.den * other.num
        newden = self.den * other.den
        factor = gcd(newnum, newden)
        self.num = int(newnum / factor)
        self.den = int(newden / factor)
        return Fraction(self.num, self.den)

    def __repr__(self):
        return "The fraction: num is {}, den is {}".format(self.num, self.den)

    def getNum(self):
        return self.num

    def getDen(self):
        return self.den

    def modify(self):
        factor = gcd(self.num, self.den)
        self.num = self.num / factor
        self.den = self.den / factor
        if isinstance(self.num, int) and isinstance(self.den, int):
            return self.__str__()
        else:
            return "not int!"


f1 = Fraction(1, 2)
f2 = Fraction(1, 3)
print(f1.__gt__(f2))
print(f1.__truediv__(f2))
print(f1.__repr__())
