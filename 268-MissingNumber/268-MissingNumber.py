# Last updated: 8/15/2026, 4:31:24 PM
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return (set(range(len(nums)+1)) - set(nums)).pop()