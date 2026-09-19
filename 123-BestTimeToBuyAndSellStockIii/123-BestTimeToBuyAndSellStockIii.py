# Last updated: 9/19/2026, 3:58:18 PM
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n = len(prices)
        sp = [-1] * n
        mp = prices[n-1]
        for i in range(n-1, -1, -1):
            mp = max(mp, prices[i])
            sp[i] = mp - prices[i]
        minp = prices[0]
        pp = 0
        ans = sp[0]

        for i in range(1, n):
            pp = max(pp, prices[i]-minp)
            minp = min(minp, prices[i])
            ans = max(ans, pp+sp[i])
        return ans