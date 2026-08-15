# Last updated: 8/15/2026, 4:29:58 PM
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)

        if len(nums) < 3:
            return max(nums)
        
        nums.remove(max(nums))
        nums.remove(max(nums))
        
        return max(nums)