# Last updated: 9/30/2026, 10:52:18 PM
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        n = len(nums)
        check = [False] * (n+1)

        for i in nums:
            if check[i]:
                return i
            check[i] = True
        return