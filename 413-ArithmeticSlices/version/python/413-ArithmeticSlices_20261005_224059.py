# Last updated: 10/5/2026, 10:40:59 PM
1class Solution:
2    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
3        cur = 0
4        s = 0
5        for i in range(2, len(nums)):
6            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
7                cur += 1
8                s += cur
9            else:
10                cur = 0
11        return s