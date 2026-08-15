# Last updated: 8/15/2026, 4:31:47 PM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False