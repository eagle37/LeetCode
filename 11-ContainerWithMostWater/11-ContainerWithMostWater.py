# Last updated: 8/22/2026, 5:45:06 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        a = 0
        while l < r:
            area = (r-l) * min(height[l], height[r])
            if area > a:
                a = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return a