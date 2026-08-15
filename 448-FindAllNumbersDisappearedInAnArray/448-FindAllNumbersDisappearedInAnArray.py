# Last updated: 8/15/2026, 4:29:44 PM
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        l = set(range(1,len(nums)+1))
        return list(l - set(nums))