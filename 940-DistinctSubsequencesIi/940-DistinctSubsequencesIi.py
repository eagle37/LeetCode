# Last updated: 9/7/2026, 11:46:36 PM
class Solution:
    MOD = 10**9 + 7
    def distinctSubseqII(self, s: str) -> int:
        tot = 0
        dp = [0] * 26

        for c in s:
            c = ord(c) - 97
            new = tot + 1 - dp[c]
            tot = (tot + new) % self.MOD
            dp[c] = (dp[c] + new) % self.MOD

        return tot