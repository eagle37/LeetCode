# Last updated: 9/2/2026, 10:56:03 PM
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        return len(s.split()[-1])