# Last updated: 10/20/2026, 10:34:01 PM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
3        m = c = 0
4
5        for i in nums:
6            if i == 1:
7                c += 1
8                m = max(m, c)
9            else:
10                c = 0
11
12        return m