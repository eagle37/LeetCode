# Last updated: 9/8/2026, 10:16:09 PM
1class Solution:
2    def compareVersion(self, version1: str, version2: str) -> int:
3        v1 = version1.split('.')
4        v2 = version2.split('.')
5
6        n = max(len(v1), len(v2))
7
8        for i in range(n):
9            a = int(v1[i]) if i < len(v1) else 0
10            b = int(v2[i]) if i < len(v2) else 0
11
12            if a > b:
13                return 1
14            elif a < b:
15                return -1
16
17        return 0