# Last updated: 10/11/2026, 11:58:02 PM
1class Solution:
2    def sumOfSquares(self, nums: List[int]) -> int:
3        l = len(nums)
4        ans = 0
5        for i in range(1, l+1):
6            if l % i == 0:
7                ans += (nums[i-1]**2)
8        return ans