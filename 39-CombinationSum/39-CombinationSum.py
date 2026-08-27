# Last updated: 8/27/2026, 4:30:48 PM
1class Solution:
2    def firstMissingPositive(self, nums: List[int]) -> int:
3
4        n = len(nums)
5
6        for i in range(n):
7
8            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
9
10                idx = nums[i] - 1
11
12                nums[i], nums[idx] = (
13                    nums[idx],
14                    nums[i]
15                )
16
17        for i in range(n):
18
19            if nums[i] != i + 1:
20                return i + 1
21
22        return n + 1