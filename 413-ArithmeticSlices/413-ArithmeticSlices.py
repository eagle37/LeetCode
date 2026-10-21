# Last updated: 10/21/2026, 9:32:46 PM
class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        cur = 0
        s = 0
        for i in range(2, len(nums)):
            if nums[i]-nums[i-1] == nums[i-1]-nums[i-2]:
                cur += 1
                s += cur
            else:
                cur = 0
        return s