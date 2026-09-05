# Last updated: 9/5/2026, 4:53:59 PM
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        sufmin = [0] * n
        sufmin[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            sufmin[i] = min(sufmin[i+1], nums[i])
        pmax = 0
        for i in range(n):
            pmax = max(pmax, nums[i])
            if pmax - sufmin[i] <= k:
                return i
        return -1