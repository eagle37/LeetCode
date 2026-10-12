# Last updated: 10/12/2026, 5:01:37 PM
1class Solution(object):
2    def numberOfBoomerangs(self, points):
3        from collections import defaultdict
4        result = 0
5        for p in points:
6            distances = defaultdict(int)
7            for q in points:
8                d = (p[0] - q[0])**2 + (p[1] - q[1])**2
9                distances[d] += 1
10            for count in distances.values():
11                result += count * (count - 1)
12        return result