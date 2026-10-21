# Last updated: 10/21/2026, 9:51:35 PM
1class Solution:
2    def nextGreaterElements(self, nums: list[int]) -> list[int]:
3        n = len(nums)
4        x = [-1] * n
5        s = []
6
7        for i in range(2 * n):
8            j = i % n
9
10            while s and nums[s[-1]] < nums[j]:
11                x[s.pop()] = nums[j]
12
13            if i < n:
14                s.append(j)
15
16        return x