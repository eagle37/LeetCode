# Last updated: 9/8/2026, 10:52:02 PM
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        ans = ''

        while columnNumber > 0:
            columnNumber -= 1
            r = columnNumber % 26
            ans = a[r] + ans
            columnNumber //= 26

        return ans