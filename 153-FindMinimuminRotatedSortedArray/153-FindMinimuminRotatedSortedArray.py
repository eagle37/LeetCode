# Last updated: 9/7/2026, 11:56:17 PM
1class Solution:
2    def findMin(self, nums: List[int]) -> int:
3        l = 0
4        r = len(nums) - 1
5        sm = nums[0]
6
7        while l <= r:
8            mid = (l + r) // 2
9
10            sm = min(sm, nums[mid])
11
12            if nums[mid] > nums[r]:
13                l = mid + 1
14            else:
15                r = mid - 1
16
17        return sm