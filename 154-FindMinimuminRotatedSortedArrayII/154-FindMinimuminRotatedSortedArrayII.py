# Last updated: 9/8/2026, 12:40:45 AM
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
12            if nums[mid] < nums[r]:
13                r = mid - 1
14            elif nums[mid] == nums[r]:
15                r -= 1
16            else:
17                l = mid + 1
18
19        return sm