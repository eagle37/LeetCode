# Last updated: 9/5/2026, 5:27:13 PM
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        c = ""
        for ch in s:
            if ch.isalnum():
                c += ch
        return c == c[::-1]         
        