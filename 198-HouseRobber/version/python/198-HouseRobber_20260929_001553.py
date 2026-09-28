# Last updated: 9/29/2026, 12:15:53 AM
1class Solution:
2    def rob(self, nums: List[int]) -> int:
3        n = len(nums)
4        
5        if n == 1:
6            return nums[0]
7        
8        dp = [0] * n
9        
10        dp[0] = nums[0]
11        dp[1] = max(nums[0], nums[1])
12        
13        for i in range(2, n):
14            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
15        
16        return dp[-1] 