# Last updated: 9/5/2026, 5:20:11 PM
1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        minp = float("inf")
4        maxp = 0
5        for p in prices:
6            if p < minp:
7                minp = p
8            p = p - minp
9            if p > maxp:
10                maxp = p
11        return maxp