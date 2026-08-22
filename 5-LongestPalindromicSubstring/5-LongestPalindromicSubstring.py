# Last updated: 8/22/2026, 6:25:50 PM
1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        prefix = ""
4        for i in range(len(strs[0])):
5            for s in strs:
6                if i >= len(s) or s[i] != strs[0][i]:
7                    return prefix
8
9            prefix += strs[0][i]
10
11        return prefix