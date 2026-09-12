# Last updated: 9/12/2026, 5:29:15 PM
1class Solution:
2    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
3        n = len(intervals)
4        arr = [
5            (intervals[i][1], intervals[i][0], intervals[i][2], i)
6            for i in range(n)
7        ]
8        arr.sort(key=lambda x: x[0])
9
10        dp = [[0] * 5 for _ in range(n + 1)]
11        indices = [[[] for _ in range(5)] for _ in range(n + 1)]
12
13        for i in range(n):
14            r, l, weight, idx = arr[i]
15            k = bisect_left(arr, (l,), hi=i)
16
17            for j in range(1, 5):
18                s1 = dp[i][j]
19                s2 = dp[k][j - 1] + weight
20                if s1 > s2:
21                    dp[i + 1][j] = dp[i][j]
22                    indices[i + 1][j] = indices[i][j].copy()
23                    continue
24
25                new_index = indices[k][j - 1].copy()
26                new_index.append(idx)
27                new_index.sort()
28                if s1 == s2 and indices[i][j] < new_index:
29                    new_index = indices[i][j].copy()
30                dp[i + 1][j] = s2
31                indices[i + 1][j] = new_index
32
33        return indices[n][4]