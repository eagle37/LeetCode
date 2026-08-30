# Last updated: 8/30/2026, 3:56:25 PM
1class Solution:
2    def minimumDeletions(self, nums: List[int]) -> int:
3
4        n = len(nums)
5
6        lowi = nums.index(min(nums))
7        highi = nums.index(max(nums))
8
9        left = min(lowi, highi)
10        right = max(lowi, highi)
11
12        a = right + 1
13
14        b = n - left
15
16        c = (left + 1) + (n - right)
17
18        return min(a, b, c)