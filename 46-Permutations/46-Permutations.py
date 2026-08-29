# Last updated: 8/29/2026, 8:31:18 PM
1class Solution:
2    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
3        nums.sort()
4        res = []
5        path = []
6        used = [False] * len(nums)
7
8        def backtrack():
9            if len(path) == len(nums):
10                res.append(path.copy())
11                return
12            
13            for i in range(len(nums)):
14                if used[i]:
15                    continue
16                if i > 0 and nums[i] == nums[i-1] and used[i-1]:
17                    continue
18                used[i] = True
19                path.append(nums[i])
20
21                backtrack()
22
23                path.pop()
24                used[i] = False
25        
26        backtrack()
27        return res