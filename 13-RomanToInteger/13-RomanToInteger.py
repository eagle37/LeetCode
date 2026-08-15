# Last updated: 8/15/2026, 4:32:46 PM
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
        x = 0
        ind = 0
        for i in range(len(s)-1):
            if ind >= len(s)-1:
                break
            a,b = s[ind].upper(), s[ind+1].upper()
            if d[a] < d[b]:
                ind += 2
                x += d[b] - d[a]
            else:
                ind += 1
                x += d[a]
            if ind >= len(s):
                break
        if ind < len(s):
            x += d[s[ind].upper()]
        return x