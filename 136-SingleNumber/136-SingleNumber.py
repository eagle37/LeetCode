# Last updated: 8/15/2026, 4:32:02 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        l = list(set(nums))
        for i in l:
            if nums.count(i) == 1:
                return i