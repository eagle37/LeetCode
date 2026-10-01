# Last updated: 10/1/2026, 10:03:15 PM
1class Solution:
2    def countNumbersWithUniqueDigits(self, n: int) -> int:
3        if n == 0:
4            return 1
5
6        ans = 10
7        curr = 9
8        x = 9
9
10        for i in range(1, n):
11            curr *= x
12            ans += curr
13            x -= 1
14
15        return ans