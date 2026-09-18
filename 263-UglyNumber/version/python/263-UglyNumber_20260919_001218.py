# Last updated: 9/19/2026, 12:12:18 AM
1class Solution:
2    def missingNumber(self, nums: list[int]) -> int:
3        n = len(nums)
4        sum1 = n * (n + 1) // 2
5        sum2 = 0
6
7        for i in range(n):
8            sum2 += nums[i]
9
10        return sum1 - sum2
11 