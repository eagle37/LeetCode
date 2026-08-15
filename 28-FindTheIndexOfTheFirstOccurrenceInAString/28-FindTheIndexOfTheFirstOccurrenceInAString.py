# Last updated: 8/15/2026, 4:32:36 PM
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle in haystack:
            return -1
        x = haystack.split(needle)
        if not x[0]:
            return 0
        return len(x[0])