# Last updated: 8/16/2026, 11:45:00 PM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        l = []
        a = 0
        b = 1

        for i in range(numRows):
            l.append([])

        for i in s:
            l[a].append(i)

            if a == numRows - 1:
                b = -1
            elif a == 0:
                b = 1

            a += b

        return ''.join(''.join(i) for i in l)