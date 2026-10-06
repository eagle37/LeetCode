# Last updated: 10/7/2026, 12:12:57 AM
1class Solution:
2    def minAddToMakeValid(self, s: str) -> int:
3        open_brackets = 0
4        min_adds_required = 0
5
6        for c in s:
7            if c == "(":
8                open_brackets += 1
9            else:
10                if open_brackets > 0:
11                    open_brackets -= 1
12                else:
13                    min_adds_required += 1
14        return min_adds_required + open_brackets