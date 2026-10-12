# Last updated: 10/12/2026, 5:08:47 PM
1class Solution:
2    def findContentChildren(self, g: list[int], s: list[int]) -> int:
3        n = len(g)
4        m = len(s)
5        l, r = 0, 0
6        g.sort()
7        s.sort()
8        while l < n and r < m:
9            if g[l] <= s[r]:
10                l += 1
11            r += 1
12        return l