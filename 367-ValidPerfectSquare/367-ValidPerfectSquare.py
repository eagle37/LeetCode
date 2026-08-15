# Last updated: 8/15/2026, 4:30:37 PM
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return (num**(1/2)).is_integer()