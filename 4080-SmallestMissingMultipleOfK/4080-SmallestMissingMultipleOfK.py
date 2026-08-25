# Last updated: 8/25/2026, 11:02:40 PM
class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        #x = k if k > len(nums)+1 else len(nums)+1
        for i in range(1, 102):
            if k*i not in nums:
                return k*i