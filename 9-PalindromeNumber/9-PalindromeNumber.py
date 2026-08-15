# Last updated: 8/15/2026, 4:32:50 PM
class Solution:
    def isPalindrome(self, x: int) -> bool:
        y = list(reversed(list(str(x))))
        if list(str(x)) == y:
            return True
        return False
        