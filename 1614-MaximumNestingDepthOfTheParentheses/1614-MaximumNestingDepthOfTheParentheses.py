# Last updated: 10/4/2026, 10:04:24 PM
class Solution:
    def maxDepth(self, s):
        depth = 0
        r = 0
        for c in s:
            if c == ')':
                depth -= 1
                continue
            if c != '(':
                continue
            depth += 1
            if depth > r:
                r = depth
        return r