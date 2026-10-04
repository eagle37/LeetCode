# Last updated: 10/4/2026, 9:51:07 PM
1class Solution:
2    def maxRotateFunction(self, nums: list[int]) -> int:
3        n = len(nums)
4        total = sum(nums)
5
6        curr = 0
7        for i in range(n):
8            curr += i * nums[i]
9
10        ans = curr
11
12        for i in range(n - 1, 0, -1):
13            curr = curr + total - n * nums[i]
14            ans = max(ans, curr)
15
16        return ans