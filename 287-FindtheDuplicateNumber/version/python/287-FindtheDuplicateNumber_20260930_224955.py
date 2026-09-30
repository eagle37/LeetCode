# Last updated: 9/30/2026, 10:49:55 PM
1class Solution:
2    def findDuplicate(self, nums: list[int]) -> int:
3        nums.sort()
4        for i in range(len(nums)-1):
5            if nums[i] == nums[i+1]:
6                return nums[i]