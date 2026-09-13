# Last updated: 9/13/2026, 7:07:50 PM
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        ans = []
        for i in nums:
            if not i in d:
                d[i] = 1
            else:
                d[i] += 1
        for i in d:
            if d[i] == 1:
                ans.append(i)
        return ans