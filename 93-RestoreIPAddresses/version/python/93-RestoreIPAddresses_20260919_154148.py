# Last updated: 9/19/2026, 3:41:48 PM
1class Solution:
2    def restoreIpAddresses(self, s: str) -> list[str]:
3        def backtrack(start, current):
4            if len(current) == 4:
5                if start == len(s):
6                    result.append('.'.join(current))
7                return
8
9            for length in range(1, 4):
10                if start + length <= len(s):
11                    segment = s[start:start+length]
12                    if self.is_valid(segment):
13                        current.append(segment)
14                        backtrack(start + length, current)
15                        current.pop()
16
17        result = []
18        backtrack(0, [])
19        return result
20
21    def is_valid(self, segment):
22        if len(segment) > 3 or (len(segment) > 1 and segment[0] == '0'):
23            return False
24        value = int(segment)
25        return 0 <= value <= 255
26