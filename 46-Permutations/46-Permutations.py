# Last updated: 8/29/2026, 8:46:27 PM
1class Solution:
2    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
3
4        groups = {}
5
6        for word in strs:
7            key = ''.join(sorted(word))
8
9            if key not in groups:
10                groups[key] = []
11
12            groups[key].append(word)
13
14        return list(groups.values())
15