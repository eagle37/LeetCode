# Last updated: 8/16/2026, 11:10:04 PM
1class Solution:
2    def reverse(self, x: int) -> int:
3        r = 0
4        sign = -1 if x < 0 else 1
5        x =  abs(x)
6        while x > 0:
7            rem = x % 10
8            x = x // 10
9            r = r * 10 + rem
10
11        if -2**31 <= r <= 2**31 - 1:
12            return r*sign
13        return 0