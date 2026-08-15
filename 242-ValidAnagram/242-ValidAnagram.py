# Last updated: 8/15/2026, 4:31:34 PM
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        for c in set(s):
            if t.count(c) != s.count(c):
                return False

        return True