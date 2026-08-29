# Last updated: 8/29/2026, 8:33:08 PM
1class Solution:
2    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
3        res = []
4
5        def backtrack(start):
6            if start == len(nums):
7                res.append(nums.copy())
8                return
9
10            seen = set()
11
12            for i in range(start, len(nums)):
13                if nums[i] in seen:
14                    continue
15
16                seen.add(nums[i])
17
18                nums[start], nums[i] = nums[i], nums[start]
19
20                backtrack(start + 1)
21
22                nums[start], nums[i] = nums[i], nums[start]
23
24        backtrack(0)
25        return res