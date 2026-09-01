# Last updated: 9/1/2026, 11:35:56 PM
1class Solution:
2    def addBinary(self, a: str, b: str) -> str:
3        if a == '0' and b == '0':
4            return "0"
5        a = int(a, 2)
6        b = int(b, 2)
7        c = a+b
8        s = ""
9        while c > 0:
10            k = c % 2
11            c = c // 2
12            s = str(k) + s
13        return s