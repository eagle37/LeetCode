# Last updated: 8/16/2026, 11:45:02 PM
class Solution:
    def reverse(self, x: int) -> int:
        r = 0
        sign = -1 if x < 0 else 1
        x =  abs(x)
        while x > 0:
            rem = x % 10
            x = x // 10
            r = r * 10 + rem

        if -2**31 <= r <= 2**31 - 1:
            return r*sign
        return 0