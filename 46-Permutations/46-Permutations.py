# Last updated: 8/29/2026, 8:51:26 PM
1class Solution:
2    def myPow(self, x: float, n: int) -> float:
3        if n < 0:
4            x = 1 / x
5            n = -n
6
7        result = 1.0
8
9        while n > 0:
10            if n % 2 == 1:
11                result *= x
12
13            x *= x
14
15            n //= 2
16
17        return result