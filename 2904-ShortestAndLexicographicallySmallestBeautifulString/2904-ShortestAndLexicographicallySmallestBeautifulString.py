# Last updated: 9/4/2026, 3:32:45 PM
class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = []

        for i in range(len(s)):
            if s[i] == '1':
                ones.append(i)

        if len(ones) < k:
            return ""

        start = 0
        end = k - 1
        best = ""

        while end < len(ones):
            l = ones[start]
            r = ones[end]

            x = s[l:r + 1]

            if not best or len(x) < len(best) or (len(x) == len(best) and x < best):
                best = x

            start += 1
            end += 1

        return best