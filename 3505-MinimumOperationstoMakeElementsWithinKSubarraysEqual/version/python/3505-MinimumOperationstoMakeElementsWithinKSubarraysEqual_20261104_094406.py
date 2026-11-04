# Last updated: 11/4/2026, 9:44:06 AM
1from sortedcontainers import SortedList
2
3class Solution:
4    def minOperations(self, nums: List[int], x: int, k: int) -> int:
5        n = len(nums)
6        vals = [None]*n
7        upper = SortedList()
8        lower = SortedList()
9        su = sl = 0 
10        for i, v in enumerate(nums): 
11            if not upper or upper[0] <= v: 
12                upper.add(v)
13                su += v
14            else: 
15                lower.add(v)
16                sl += v
17            if i >= x: 
18                vv = nums[i-x]
19                if vv >= upper[0]: 
20                    upper.remove(vv)
21                    su -= vv
22                else: 
23                    lower.remove(vv)
24                    sl -= vv
25            while len(upper) > len(lower)+1: 
26                v = upper[0]
27                upper.remove(v)
28                su -= v
29                lower.add(v)
30                sl += v
31            while len(upper) < len(lower): 
32                v = lower[-1]
33                lower.remove(v)
34                sl -= v
35                upper.add(v)
36                su += v
37            if i >= x-1: vals[i-x+1] = su - sl - upper[0]*(len(upper)-len(lower))
38    
39        dp = [[inf]*(k+1) for _ in range(n+1)]
40        for i in range(n, -1, -1): 
41            dp[i][0] = 0
42            for j in range(1, k+1): 
43                if n-i >= j*x: 
44                    dp[i][j] = min(dp[i+1][j], vals[i] + dp[i+x][j-1])
45        return dp[0][k]