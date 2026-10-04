# Last updated: 10/4/2026, 7:58:04 PM
1class Solution:
2    def checkValidString(self, s: str) -> bool:
3        low = 0
4        high = 0
5
6        for ch in s:
7            if ch == '(':
8                low += 1
9                high += 1
10            elif ch == ')':
11                if low > 0:
12                    low -= 1
13                high -= 1
14            else:
15                if low > 0:
16                    low -= 1
17                high += 1
18
19            if high < 0:
20                return False
21
22        return low == 0