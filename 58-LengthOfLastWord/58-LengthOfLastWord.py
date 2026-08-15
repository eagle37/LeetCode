# Last updated: 8/15/2026, 4:32:30 PM
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        v = s.split()
        return len(v[-1])