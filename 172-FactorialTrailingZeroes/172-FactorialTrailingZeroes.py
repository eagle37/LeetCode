# Last updated: 9/9/2026, 10:21:12 PM
1class Solution:
2    def trailingZeroes(self, n: int) -> int:
3        count = 0
4        power = 5
5
6        while power <= n:
7            count += n//power
8            power *= 5
9        
10        return count