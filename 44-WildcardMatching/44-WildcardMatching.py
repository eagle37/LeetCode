# Last updated: 8/28/2026, 10:16:58 PM
1class Solution:
2    def jump(self, nums):
3        jumps = 0
4        cur = 0
5        farthest = 0
6
7        for i in range(len(nums) - 1):
8
9            farthest = max(farthest, i + nums[i])
10
11            if i == cur:
12                jumps += 1
13                cur = farthest
14
15        return jumps