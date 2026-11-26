# Last updated: 11/26/2026, 10:06:20 AM
1class Solution:
2    def canAliceWin(self, n: int) -> bool:
3        
4        for stones in (19, 15, 11, 7, 3):
5
6            if n >= stones: n-= stones
7               
8            else: return n >= stones//2 +1
9
10        return True