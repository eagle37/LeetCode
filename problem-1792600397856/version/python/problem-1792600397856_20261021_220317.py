# Last updated: 10/21/2026, 10:03:17 PM
1class Solution:
2    def checkPerfectNumber(self, num: int) -> bool:
3        if num <= 1:
4            return False
5
6        s = 1
7        i = 2
8
9        while i * i <= num:
10            if num % i == 0:
11                s += i
12                if i != num // i:
13                    s += num // i
14            i += 1
15
16        return s == num