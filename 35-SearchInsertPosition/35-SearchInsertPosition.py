# Last updated: 8/15/2026, 4:32:33 PM
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target not in nums:
            if target < nums[0]:
                return 0
            for i in range(len(nums)-1):
                if target > nums[i] and target < nums[i+1]:
                    return i+1
            else:
                return len(nums)
        else:
            return nums.index(target)