# Last updated: 9/5/2026, 5:24:49 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        return "".join([ch for ch in s if ch.isalnum()]).lower() == "".join([ch for ch in s if ch.isalnum()])[::-1].lower()