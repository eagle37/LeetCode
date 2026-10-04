# Last updated: 10/4/2026, 10:05:29 PM
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        x = [False]*(n+1)
        for i in nums:
            if x[i]:
                return i
            x[i] = True
        