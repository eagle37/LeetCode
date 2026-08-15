# Last updated: 8/15/2026, 4:29:45 PM
class Solution:
    def arrangeCoins(self, n: int) -> int:
        row = 1
        while n >= row:
            n -= row
            row += 1
        return row - 1
