# Last updated: 9/8/2026, 10:06:24 PM
1class Solution:
2    def findPeakElement(self, nums: List[int]) -> int:
3        if len(nums) == 1:
4            return 0
5        l = 0
6        r = len(nums)-1
7        while l < r:
8            mid = (l+r)//2
9            if nums[mid] < nums[mid+1]:
10                l = mid+1
11            elif nums[mid] > nums[mid+1]:
12                r = mid
13        return l