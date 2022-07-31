# https://leetcode.com/problems/complex-number-multiplication/

class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        num1 = num1.split('+')
        num2 = num2.split('+')
        a = int(num1[0])
        b = int(num1[1][:-1])
        c = int(num2[0])
        d = int(num2[1][:-1])
        real = a * c - b * d
        im = a * d + b * c
        res = str(real) + '+' + str(im) + 'i'
        return res