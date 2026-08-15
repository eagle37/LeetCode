# Last updated: 8/15/2026, 4:32:58 PM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}
        for i, num in enumerate(nums):
                if target-num in s:
                    return [s[target-num], i]
                s[num] = i
        return []
