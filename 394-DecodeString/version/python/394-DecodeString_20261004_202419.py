# Last updated: 10/4/2026, 8:24:19 PM
1class Solution(object):
2    def decodeString(self, s):
3        stack = []; curNum = 0; curString = ''
4        for c in s:
5            if c == '[':
6                stack.append(curString)
7                stack.append(curNum)
8                curString = ''
9                curNum = 0
10            elif c == ']':
11                num = stack.pop()
12                prevString = stack.pop()
13                curString = prevString + num*curString
14            elif c.isdigit():
15                curNum = curNum*10 + int(c)
16            else:
17                curString += c
18        return curString