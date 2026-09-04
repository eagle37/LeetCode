# Last updated: 9/4/2026, 3:23:21 PM
class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:

        n = len(nums)

        lowi = nums.index(min(nums))
        highi = nums.index(max(nums))

        left = min(lowi, highi)
        right = max(lowi, highi)

        a = right + 1

        b = n - left

        c = (left + 1) + (n - right)

        return min(a, b, c)