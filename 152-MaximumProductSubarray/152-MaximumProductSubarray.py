# Last updated: 9/6/2026, 11:53:08 PM
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = nums[0]
        currMin = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                currMax, currMin = currMin, currMax

            currMax = max(nums[i], currMax * nums[i])
            currMin = min(nums[i], currMin * nums[i])

            ans = max(ans, currMax)

        return ans