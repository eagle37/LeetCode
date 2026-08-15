# Last updated: 8/15/2026, 4:30:21 PM
from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        r, m = Counter(ransomNote), Counter(magazine)
        for ch in r:
            if r[ch] > m[ch]:
                return False
        return True
