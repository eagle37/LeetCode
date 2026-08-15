# Last updated: 8/15/2026, 4:31:05 PM
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0