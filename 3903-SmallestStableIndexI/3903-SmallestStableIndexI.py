# Last updated: 9/4/2026, 3:32:21 PM
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)
        for i in range(n):
            minv, maxv = nums[i], nums[i]
            for j in range(i):
                maxv = max(maxv, nums[j])
            for j in range(i+1, n):
                minv = min(minv, nums[j])
            if maxv - minv <= k:
                return i
        return -1