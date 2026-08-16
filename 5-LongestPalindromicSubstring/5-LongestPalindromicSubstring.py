# Last updated: 8/16/2026, 11:42:58 PM
1class Solution:
2    def myAtoi(self, s: str) -> int:
3        res = 0
4        sign = 1
5        s = s.lstrip()
6
7        if not s:
8            return 0
9
10        if s[0] == "+":
11            sign = 1
12        elif s[0] == "-":
13            sign = -1
14
15        for i in range(len(s)):
16            if i == 0 and s[i] in ("+", "-"):
17                continue
18            elif not "0" <= s[i] <= "9":
19                break
20            else:
21                res = res * 10 + int(s[i])
22
23        res *= sign
24        return max(-2**31, min(res, 2**31 - 1))