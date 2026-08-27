# Last updated: 8/27/2026, 4:32:04 PM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        n = len(nums)

        for i in range(n):

            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:

                idx = nums[i] - 1

                nums[i], nums[idx] = (
                    nums[idx],
                    nums[i]
                )

        for i in range(n):

            if nums[i] != i + 1:
                return i + 1

        return n + 1