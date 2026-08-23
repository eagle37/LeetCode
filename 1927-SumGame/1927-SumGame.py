# Last updated: 8/23/2026, 5:22:46 PM
1class Solution:
2    def sumGame(self, num: str) -> bool:
3        ql, qr, diff = 0, 0, 0
4        n = len(num)
5        half = n // 2
6        for i in range(n):
7            if i < half:
8                if num[i] == '?':
9                    ql += 1
10                else:
11                    diff += int(num[i])
12            else:
13                if num[i] == '?':
14                    qr += 1
15                else:
16                    diff -= int(num[i])
17        if (ql+qr) % 2 != 0:
18            return True
19        return diff != 9 * (qr-ql) // 2