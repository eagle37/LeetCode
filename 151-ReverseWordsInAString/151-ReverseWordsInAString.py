# Last updated: 9/6/2026, 11:53:09 PM
class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        y = ''
        for i in x[::-1]:
            if len(i) > 0:
                y += i + " "
        return y[:len(y)-1]