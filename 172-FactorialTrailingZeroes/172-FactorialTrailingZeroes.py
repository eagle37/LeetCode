# Last updated: 9/9/2026, 10:19:22 PM
1class Solution:
2    def trailingZeroes(self, n: int) -> int:
3        ans = 1
4        for i in range(1, n+1):
5            ans *= i
6        cnt = 0
7        while ans % 10 == 0:
8            cnt += 1
9            ans = ans // 10
10        return cnt