# Last updated: 8/15/2026, 4:31:12 PM
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(pattern) != len(s):
            return False
        d = {}
        d_ = {}
        for i in range(len(pattern)):
            if (pattern[i] in d and d[pattern[i]] != s[i]) or s[i] in d_ and d_[s[i]] != pattern[i]:
                return False
            else:
                d[pattern[i]] = s[i]
                d_[s[i]] = pattern[i]
        return True