# Last updated: 10/12/2026, 5:04:11 PM
1class Solution(object):
2    def minMoves(self, nums):
3        from functools import reduce
4        return reduce(lambda a, b: a + b, nums) - len(nums) * min(nums)