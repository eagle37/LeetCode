# Last updated: 10/4/2026, 8:12:41 PM
1class Solution:
2    def getSum(self, a: int, b: int) -> int:
3        mask = 0xffffffff
4
5        while b:
6            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
7
8        if a > 0x7fffffff:
9            return ~((a ^ mask))
10
11        return a