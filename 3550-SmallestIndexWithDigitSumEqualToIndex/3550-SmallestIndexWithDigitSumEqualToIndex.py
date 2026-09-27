# Last updated: 9/27/2026, 7:08:09 PM
class Solution:
    def smallestIndex(self, nums):

        for i in range(len(nums)):
            x = nums[i]
            total = 0

            while x > 0:
                total += x % 10
                x //= 10

            if total == i:
                return i

        return -1