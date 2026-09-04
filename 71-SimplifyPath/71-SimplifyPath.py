# Last updated: 9/4/2026, 3:44:29 PM
1class Solution:
2    def simplifyPath(self, path: str) -> str:
3        a = []
4        for i in path.split("/"):
5            if i == '.' or i == '..':
6                if len(a) > 0 and i == '..':
7                    a.pop()
8                else:
9                    pass
10            elif i:
11                a.append(i)
12        s = "/" + "/".join([x for x in a[0:len(a)]])
13        return s[:len(s)]