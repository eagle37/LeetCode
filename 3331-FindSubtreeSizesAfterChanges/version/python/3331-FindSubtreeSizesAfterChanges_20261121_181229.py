# Last updated: 11/21/2026, 6:12:29 PM
1    
2class Solution:
3    def findSubtreeSizes(self, p: List[int], s: str) -> List[int]:
4        n = len(p)
5        adj = [[] for _ in range(n)]
6        tree = [[] for _ in range(n)]
7        ans = [0] * n
8        last = [-1] * 26
9
10        for i in range(1, n):
11            adj[p[i]].append(i)
12
13        def dfs(u):
14            c = ord(s[u]) - ord('a')
15            old = last[c]
16
17            if u and old != -1:
18                p[u] = old
19            last[c] = u
20
21            for v in adj[u]:
22                dfs(v)
23
24            last[c] = old
25
26        def calc(u):
27            ans[u] = 1
28            for v in tree[u]:
29                ans[u] += calc(v)
30            return ans[u]
31
32        dfs(0)
33
34        for i in range(1, n):
35            tree[p[i]].append(i)
36
37        calc(0)
38        return ans