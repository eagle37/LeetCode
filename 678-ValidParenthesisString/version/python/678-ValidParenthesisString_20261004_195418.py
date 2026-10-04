# Last updated: 10/4/2026, 7:54:18 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        l = h = 0
4
5        for c in s:
6            l += ((c == '(') << 1) - 1
7            h += ((c != ')') << 1) - 1
8
9            if h < 0: return False
10
11            l = max(l, 0)
12
13        return l == 0