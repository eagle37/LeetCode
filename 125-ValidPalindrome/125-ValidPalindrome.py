# Last updated: 8/15/2026, 4:32:03 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        x = "".join([ch for ch in s if ch.isalnum()]).lower()
        return x == x[::-1]