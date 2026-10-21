# Last updated: 10/21/2026, 9:32:18 PM
class Solution(object):
    def minMoves(self, nums):
        from functools import reduce
        return reduce(lambda a, b: a + b, nums) - len(nums) * min(nums)