# Last updated: 8/15/2026, 10:35:40 PM
1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        _ = 0
4        __ = set()
5        ___ = 0
6
7        for i in range(len(s)):
8            while s[i] in __:
9                __.remove(s[_])
10                _ += 1
11
12            __.add(s[i])
13            ___ = max(___, i - _ + 1)
14
15        return ___