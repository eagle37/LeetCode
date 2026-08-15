# Last updated: 8/15/2026, 4:31:10 PM
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 1162261467 % n == 0