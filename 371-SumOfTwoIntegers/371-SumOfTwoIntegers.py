# Last updated: 10/4/2026, 10:05:09 PM
class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff

        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        if a > 0x7fffffff:
            return ~((a ^ mask))

        return a