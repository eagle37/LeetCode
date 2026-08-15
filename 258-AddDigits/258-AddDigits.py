# Last updated: 8/15/2026, 4:31:30 PM
class Solution:
    def addDigits(self, num: int) -> int:
        def rec(n):
            x = 0
            if n < 10:
                return n
            while n >= 1:
                x += n % 10
                n = n//10
            return rec(x)

        return rec(num)