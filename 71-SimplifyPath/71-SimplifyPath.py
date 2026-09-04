# Last updated: 9/4/2026, 4:04:31 PM
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        k = 2
        for i in range(2,n):
            if nums[i] != nums[k - 2]:
                nums[k] = nums[i]
                k += 1
        return k