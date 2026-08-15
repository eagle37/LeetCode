# Last updated: 8/15/2026, 4:29:50 PM
class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d = {}
        m = 0
        for i in nums:
            if i not in d:
                d[i] = nums.count(i)
        l = list(d.values())
        x = max(l)
        for i_ in l:
            if i_ == x:
                m+=x
        return m
