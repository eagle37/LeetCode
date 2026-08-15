# Last updated: 8/15/2026, 4:32:17 PM
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        a,b=1,2
        for i in range(3,n+1):
            a,b = b,a+b
        return b