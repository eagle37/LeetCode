# Last updated: 8/30/2026, 4:08:30 PM
1class Solution:
2    def canJump(self, nums: List[int]) -> bool:
3        i = 0
4        res = False
5        for j in range(len(nums)):
6            if i < j:
7                return res
8            i = max(i, j+nums[j])
9            if i >= len(nums)-1:
10                return True