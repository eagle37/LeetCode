# Last updated: 10/21/2026, 9:31:44 PM
class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        sqrt = math.isqrt(area)
        for i in range(sqrt, 0, -1):
            if area % i == 0:
                return [area//i, i]