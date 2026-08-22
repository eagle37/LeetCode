# Last updated: 8/22/2026, 2:03:55 PM
1class Solution:
2    def checkDivisibility(self, n: int) -> bool:
3        _ = 0
4        __ = 1
5        ___ = n
6        while ___ >= 1:
7            ____ = ___ % 10
8            _ += ____
9            __ *= ____
10            ___ = ___ // 10
11        if n % (_+__) == 0:
12            return True
13        return False