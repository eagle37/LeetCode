# Last updated: 8/15/2026, 4:31:59 PM
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]