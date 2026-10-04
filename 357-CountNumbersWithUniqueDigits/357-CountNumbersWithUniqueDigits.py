# Last updated: 10/4/2026, 10:05:12 PM
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        ans = 10
        curr = 9
        x = 9

        for i in range(1, n):
            curr *= x
            ans += curr
            x -= 1

        return ans