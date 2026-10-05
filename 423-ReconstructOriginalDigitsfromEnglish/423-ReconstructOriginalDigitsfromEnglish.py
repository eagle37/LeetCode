# Last updated: 10/5/2026, 10:51:25 PM
1class Solution(object):
2    def originalDigits(self, s: str) -> str:
3        from collections import Counter
4        c = Counter(s)
5        d = {}
6        d[0] = c['z']
7        d[2] = c['w']
8        d[4] = c['u']
9        d[6] = c['x']
10        d[8] = c['g']
11        d[1] = c['o'] - d[0] - d[2] - d[4]
12        d[3] = c['h'] - d[8]
13        d[5] = c['f'] - d[4]
14        d[7] = c['s'] - d[6]
15        d[9] = c['i'] - d[5] - d[6] - d[8]
16        return ''.join(str(i) * d[i] for i in range(10))