# Last updated: 8/23/2026, 5:57:56 PM
1class Solution:
2    def threeSumClosest(self, nums: List[int], target: int) -> int:
3        nums.sort()
4        best = nums[0]+nums[1]+nums[2]
5        for i in range(len(nums)):
6            l, r = i+1, len(nums)-1
7            while l < r:
8                sm = nums[i] + nums[l] + nums[r]
9                if abs(sm - target) < abs(best - target):
10                    best = sm
11                if sm < target:
12                    l += 1
13                elif sm > target:
14                    r -= 1
15                else:
16                    break
17        return best