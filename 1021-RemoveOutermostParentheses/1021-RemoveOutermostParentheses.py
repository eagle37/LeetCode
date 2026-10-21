# Last updated: 10/21/2026, 9:31:14 PM
class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res, lvl = [], 0

        for c in s:
            if c == ")":
                lvl -= 1
            if lvl > 0:
                res.append(c)
            if c == "(":
                lvl += 1
                
        return "".join(res)