# Last updated: 10/20/2026, 10:53:13 PM
1class Solution:
2    def constructRectangle(self, area: int) -> list[int]:
3        sqrt = math.isqrt(area)
4        for i in range(sqrt, 0, -1):
5            if area % i == 0:
6                return [area//i, i]