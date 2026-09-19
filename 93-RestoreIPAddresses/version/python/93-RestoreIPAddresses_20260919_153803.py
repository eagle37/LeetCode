# Last updated: 9/19/2026, 3:38:03 PM
1class Solution:
2    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
3        m, n, l = len(s1), len(s2), len(s3)
4        if m + n != l:
5            return False
6        
7        if m < n:
8            return self.isInterleave(s2, s1, s3)
9        
10        dp = [False] * (n + 1)
11        dp[0] = True
12        
13        for j in range(1, n + 1):
14            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]
15        
16        for i in range(1, m + 1):
17            dp[0] = dp[0] and s1[i-1] == s3[i-1]
18            for j in range(1, n + 1):
19                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or (dp[j-1] and s2[j-1] == s3[i+j-1])
20        
21        return dp[n]