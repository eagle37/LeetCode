# Last updated: 8/22/2026, 5:42:49 PM
1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l = 0
4        r = len(height)-1
5        a = 0
6        while l < r:
7            area = (r-l) * min(height[l], height[r])
8            if area > a:
9                a = area
10            if height[l] < height[r]:
11                l += 1
12            else:
13                r -= 1
14        return a