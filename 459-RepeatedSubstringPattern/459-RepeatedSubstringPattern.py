# Last updated: 10/21/2026, 9:32:07 PM
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        for length in range(1, n):
            if n % length == 0:
                pattern = s[:length]

                if pattern * (n // length) == s:
                    return True

        return False