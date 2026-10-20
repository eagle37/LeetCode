# Last updated: 10/20/2026, 11:55:18 PM
1class Solution:
2    def findWords(self, words: list[str]) -> list[str]:
3        d = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
4        ans = []
5
6        for i in words:
7            r = None
8
9            for j in i.lower():
10                if r is None:
11                    if j in d[0]:
12                        r = 0
13                    elif j in d[1]:
14                        r = 1
15                    else:
16                        r = 2
17                elif j not in d[r]:
18                    break
19            else:
20                ans.append(i)
21
22        return ans