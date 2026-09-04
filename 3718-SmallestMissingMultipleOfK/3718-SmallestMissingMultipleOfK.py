# Last updated: 9/4/2026, 3:32:23 PM
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        #x = k if k > len(nums)+1 else len(nums)+1
        for i in range(1, 102):
            if k*i not in nums:
                return k*i