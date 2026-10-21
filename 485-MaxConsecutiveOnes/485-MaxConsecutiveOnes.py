# Last updated: 10/21/2026, 9:31:51 PM
class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        m = 0
        c = 0

        for i in nums:
            if i == 1:
                c += 1
            else:
                if m < c:
                    m = c
                c = 0

        return max(m, c)