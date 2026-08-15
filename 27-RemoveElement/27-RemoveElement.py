# Last updated: 8/15/2026, 4:32:40 PM
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        x = 0
        for i in nums:
            if i == val:
                x+= 1

        for i in range(x):
            nums.remove(val)
        
        return len(nums)