# Last updated: 10/21/2026, 9:30:38 PM
class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        left = sum(x < target for x in nums)
        right = sum(x <= target for x in nums)
        return list(range(left, right))