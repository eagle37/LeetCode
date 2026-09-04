# Last updated: 9/4/2026, 3:32:38 PM
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
