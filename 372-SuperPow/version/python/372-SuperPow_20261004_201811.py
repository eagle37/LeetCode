# Last updated: 10/4/2026, 8:18:11 PM
1class Solution:
2    def superPow(self, a: int, b: list[int]) -> int:
3        ans = 1
4
5        for i in b:
6            ans = pow(ans, 10, 1337) * pow(a, i, 1337)
7            ans %= 1337
8
9        return ans