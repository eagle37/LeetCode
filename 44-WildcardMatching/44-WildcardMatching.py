# Last updated: 8/28/2026, 9:58:19 PM
1class Solution:
2    def isMatch(self, s: str, p: str) -> bool:
3        m, n = len(s), len(p)
4
5        dp = [[False] * (n + 1) for _ in range(m + 1)]
6        dp[m][n] = True
7
8        for i in range(m, -1, -1):
9            for j in range(n - 1, -1, -1):
10
11                if p[j] == '*':
12                    dp[i][j] = dp[i][j + 1]
13
14                    if i < m:
15                        dp[i][j] |= dp[i + 1][j]
16
17                elif i < m and (p[j] == s[i] or p[j] == '?'):
18                    dp[i][j] = dp[i + 1][j + 1]
19
20        return dp[0][0]