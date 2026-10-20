# Last updated: 10/20/2026, 11:11:48 PM
1class Solution(object):
2    def findPoisonedDuration(self, timeSeries, duration):
3        res = 0
4        n = len(timeSeries)
5
6        for i in range(n - 1):
7            d = timeSeries[i + 1] - timeSeries[i]
8            res += duration if d > duration else d
9
10        return res + duration