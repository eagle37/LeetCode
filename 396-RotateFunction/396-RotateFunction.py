# Last updated: 10/4/2026, 10:04:53 PM
class Solution:
    def maxRotateFunction(self, nums: list[int]) -> int:
        n = len(nums)
        total = sum(nums)

        curr = 0
        for i in range(n):
            curr += i * nums[i]

        ans = curr

        for i in range(n - 1, 0, -1):
            curr = curr + total - n * nums[i]
            ans = max(ans, curr)

        return ans