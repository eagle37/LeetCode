# Last updated: 9/4/2026, 4:04:15 PM
1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        k = 2
4
5        for i in range(2, len(nums)):
6            if nums[i] != nums[k - 2]:
7                nums[k] = nums[i]
8                k += 1
9
10        return k