# Last updated: 10/1/2026, 8:38:43 PM
1class Solution:
2    def isValid(self, s: str) -> bool:
3        if len(s) % 2 != 0:
4            return False
5        l = []
6        for i in s:
7            if i in '({[':
8                l.append(i)
9            else:
10                if len(l) == 0:
11                    return False
12                if i == ')' and l[-1] == '(':
13                    l.pop()
14                elif i == ')' and l[-1] != '(':
15                    return False
16                elif i == ']' and l[-1] == '[':
17                    l.pop()
18                elif i == ']' and l[-1] != '[':
19                    return False
20                elif i == '}' and l[-1] == '{':
21                    l.pop()
22                elif i == '}' and l[-1] != '{':
23                    return False
24        return len(l) == 0