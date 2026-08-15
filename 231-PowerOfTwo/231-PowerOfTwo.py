# Last updated: 8/15/2026, 4:31:39 PM
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n - 1)) == 0