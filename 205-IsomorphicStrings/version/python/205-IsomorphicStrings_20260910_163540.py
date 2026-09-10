# Last updated: 9/10/2026, 4:35:40 PM
1
2class Solution(object):
3    def isIsomorphic(self, s, t):
4        map1 = []
5        map2 = []
6        for idx in s:
7            map1.append(s.index(idx))
8        for idx in t:
9            map2.append(t.index(idx))
10        if map1 == map2:
11            return True
12        return False