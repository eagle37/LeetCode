# Last updated: 8/22/2026, 5:44:02 PM
class Solution:
    def checkDivisibility(self, n: int) -> bool:
        _ = 0
        __ = 1
        ___ = n
        while ___ >= 1:
            ____ = ___ % 10
            _ += ____
            __ *= ____
            ___ = ___ // 10
        if n % (_+__) == 0:
            return True
        return False