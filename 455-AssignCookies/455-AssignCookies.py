# Last updated: 10/21/2026, 9:32:14 PM
class Solution:
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        n = len(g)
        m = len(s)
        l, r = 0, 0
        g.sort()
        s.sort()
        while l < n and r < m:
            if g[l] <= s[r]:
                l += 1
            r += 1
        return l