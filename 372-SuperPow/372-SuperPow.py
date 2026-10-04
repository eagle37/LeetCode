# Last updated: 10/4/2026, 10:05:06 PM
class Solution:
    def superPow(self, a: int, b: list[int]) -> int:
        ans = 1

        for i in b:
            ans = pow(ans, 10, 1337) * pow(a, i, 1337)
            ans %= 1337

        return ans