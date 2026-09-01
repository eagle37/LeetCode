# Last updated: 9/1/2026, 11:37:25 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return "0"
        a = int(a, 2)
        b = int(b, 2)
        c = a+b
        s = ""
        while c > 0:
            k = c % 2
            c = c // 2
            s = str(k) + s
        return s
