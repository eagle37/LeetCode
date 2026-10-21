# Last updated: 10/21/2026, 9:30:22 PM
class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        l = len(nums)
        ans = 0
        for i in range(1, l+1):
            if l % i == 0:
                ans += (nums[i-1]**2)
        return ans