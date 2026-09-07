# Last updated: 9/8/2026, 12:43:47 AM
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        sm = nums[0]

        while l <= r:
            mid = (l + r) // 2

            sm = min(sm, nums[mid])

            if nums[mid] < nums[r]:
                r = mid - 1
            elif nums[mid] == nums[r]:
                r -= 1
            else:
                l = mid + 1

        return sm