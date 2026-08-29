# Last updated: 8/29/2026, 8:46:14 PM
1import typing
2from typing import List
3class Solution:
4    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
5
6        groups = {}
7
8        for word in strs:
9            key = ''.join(sorted(word))
10
11            if key not in groups:
12                groups[key] = []
13
14            groups[key].append(word)
15
16        return list(groups.values())
17      
18c = Solution()
19s = c.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
20print(s)