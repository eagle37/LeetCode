# Last updated: 9/9/2026, 10:16:07 PM
1class Solution:
2    def countCommas(self, n: int) -> int:
3        ans = 0
4        power = 1000
5
6        while power <= n:
7            ans += n - power + 1
8            power *= 1000
9
10        return ans