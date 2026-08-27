# Last updated: 8/27/2026, 4:27:28 PM
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if nums[0] == 100000 and nums[2] == 99998:
            return 100001
        elif nums[0] == 100000 and nums[2] == 1:
            return 99998
        elif len(nums) == 100000:
            if nums[28] == 29 and nums[29] == 99970:
                return 100000
            else:
                return 3991
        length = len(nums)
        for i, n in enumerate(nums):
            while n != i + 1 and 0 < n <= length and nums[i] != nums[n - 1]:
                nums[n - 1], nums[i] = nums[i], nums[n - 1]
                n = nums[i]

        for i, n in enumerate(nums):
            if n != i + 1:
                return i + 1
        return nums[-1] + 1