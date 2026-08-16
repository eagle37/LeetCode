# Last updated: 8/16/2026, 11:00:29 PM
1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1:
4            return s
5
6        l = []
7        a = 0
8        b = 1
9
10        for i in range(numRows):
11            l.append([])
12
13        for i in s:
14            l[a].append(i)
15
16            if a == numRows - 1:
17                b = -1
18            elif a == 0:
19                b = 1
20
21            a += b
22
23        return ''.join(''.join(i) for i in l)