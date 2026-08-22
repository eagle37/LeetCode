# Last updated: 8/22/2026, 5:43:17 PM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        vol = 0
        l, r, max_height = 0, len(height) - 1, max(height)
        while l < r:
            vol = max(vol, min(height[l], height[r]) * (r - l))
            if vol >= max_height * (r - l):
                return vol
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return vol