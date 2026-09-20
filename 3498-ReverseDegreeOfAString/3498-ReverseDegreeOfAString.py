# Last updated: 9/20/2026, 7:34:51 PM
class Solution:
    def reverseDegree(self, s: str) -> int:
        a = 0
        y = 1
        for i in s:
            a = a + ((123-ord(i))*y)
            y += 1
        return a