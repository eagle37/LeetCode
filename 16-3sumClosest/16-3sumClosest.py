# Last updated: 8/23/2026, 6:30:20 PM
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = nums[0]+nums[1]+nums[2]
        for i in range(len(nums)):
            l, r = i+1, len(nums)-1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if abs(sm - target) < abs(best - target):
                    best = sm
                if sm < target:
                    l += 1
                elif sm > target:
                    r -= 1
                else:
                    break
        return best