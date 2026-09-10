# Last updated: 9/10/2026, 9:50:30 PM
1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def averageOfSubtree(self, root: TreeNode) -> int:
9        ans = 0
10
11        def dfs(node):
12            nonlocal ans
13
14            if node is None:
15                return 0, 0
16
17            ls, lc = dfs(node.left)
18            rs, rc = dfs(node.right)
19
20            s = ls + rs + node.val
21            c = lc + rc + 1
22
23            if s // c == node.val:
24                ans += 1
25
26            return s, c
27
28        dfs(root)
29        return ans