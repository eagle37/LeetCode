# Last updated: 8/22/2026, 5:26:30 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        n = len(s)
4        res = ""
5
6        for i in range(n):
7            st = end = i
8            while st >= 0 and end < n and s[st] == s[end]:
9                st -= 1
10                end += 1
11            temp = s[st+1:end]
12            if len(temp) > len(res):
13                res = temp
14            st, end = i, i+1
15            while st >= 0 and end < n and s[st] == s[end]:
16                st -= 1
17                end += 1
18            temp = s[st+1:end]
19            if len(temp) > len(res):
20                res = temp
21
22        return res