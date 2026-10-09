# Last updated: 10/9/2026, 10:26:05 PM
1class Solution:
2    def minInsertions(self, s: str) -> int:
3        open = ans = 0
4        i = 0
5
6        while i < len(s):
7            if s[i] == '(':
8                open += 1
9            else:
10                # Step 1: make a "))"
11                if i + 1 < len(s) and s[i + 1] == ')':
12                    i += 1
13                else:
14                    ans += 1
15
16                # Step 2: find its '('
17                if open > 0:
18                    open -= 1
19                else:
20                    ans += 1
21            i += 1
22
23        return ans + open * 2