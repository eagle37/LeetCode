# Last updated: 10/20/2026, 10:52:39 PM
1class Solution:
2    def constructRectangle(self, area: int) -> list[int]:
3        sqrt = math.isqrt(area)
4        for i in range(sqrt, 0, -1):
5            if (area/i).is_integer():
6                return [int(area/i), i]