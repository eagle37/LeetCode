# Last updated: 8/16/2026, 11:44:58 PM
class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        sign = 1
        s = s.lstrip()

        if not s:
            return 0

        if s[0] == "+":
            sign = 1
        elif s[0] == "-":
            sign = -1

        for i in range(len(s)):
            if i == 0 and s[i] in ("+", "-"):
                continue
            elif not "0" <= s[i] <= "9":
                break
            else:
                res = res * 10 + int(s[i])

        res *= sign
        return max(-2**31, min(res, 2**31 - 1))