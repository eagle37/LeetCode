# Last updated: 11/24/2026, 9:47:52 PM
1class Solution:
2    def maxLength(self, nums: list[int]) -> int:
3        best, left, product = 2, 0, 1
4        for right, x in enumerate(nums):
5            while gcd(product, x) > 1:
6                product //= nums[left]
7                left += 1
8            product *= x
9            best = max(best, right - left + 1)
10        return best