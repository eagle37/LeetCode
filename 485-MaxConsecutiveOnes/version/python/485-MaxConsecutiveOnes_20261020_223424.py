# Last updated: 10/20/2026, 10:34:24 PM
1class Solution:
2    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
3        m = 0
4        c = 0
5
6        for i in nums:
7            if i == 1:
8                c += 1
9            else:
10                if m < c:
11                    m = c
12                c = 0
13
14        return max(m, c)