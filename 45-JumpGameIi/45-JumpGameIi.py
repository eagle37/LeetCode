# Last updated: 9/4/2026, 3:24:38 PM
class Solution:
    def jump(self, nums):
        jumps = 0
        cur = 0
        farthest = 0

        for i in range(len(nums) - 1):

            farthest = max(farthest, i + nums[i])

            if i == cur:
                jumps += 1
                cur = farthest

        return jumps