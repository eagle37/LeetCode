# Last updated: 8/29/2026, 8:28:59 PM
1class Solution:
2    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
3        res = []
4        path = []
5        used = [False] * len(nums)
6
7        def backtrack():
8            if len(path) == len(nums) and path not in res:
9                res.append(path.copy())
10                return
11            
12            for i in range(len(nums)):
13                if used[i]:
14                    continue
15                
16                used[i] = True
17                path.append(nums[i])
18
19                backtrack()
20
21                path.pop()
22                used[i] = False
23        
24        backtrack()
25        return res