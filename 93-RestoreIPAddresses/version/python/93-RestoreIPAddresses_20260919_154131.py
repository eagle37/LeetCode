# Last updated: 9/19/2026, 3:41:31 PM
1class Solution:
2    def minimumTotal(self, triangle: List[List[int]]) -> int:
3        row = len(triangle)
4        memo = triangle[row-1].copy()
5
6        for r in range(row-2, -1, -1):
7            for c in range(r+1):
8                memo[c] = min(memo[c], memo[c+1]) + triangle[r][c]
9        
10        return memo[0]