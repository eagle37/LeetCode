# Last updated: 9/2/2026, 11:09:42 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        for i in range(len(nums)):
7            for j in range(len(nums)-i-1):
8                if nums[j] > nums[j+1]:
9                    nums[j], nums[j+1] = nums[j+1], nums[j]
10        