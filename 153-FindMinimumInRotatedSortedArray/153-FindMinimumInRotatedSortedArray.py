# Last updated: 9/8/2026, 12:43:50 AM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        sm = nums[0]

        while l <= r:
            mid = (l + r) // 2

            sm = min(sm, nums[mid])

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return sm