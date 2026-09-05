# Last updated: 9/5/2026, 5:29:24 PM
1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        x = ''
4        for i in range(len(s)):
5            if s[i].isalnum():
6                x += s[i].lower()
7        return x == x[::-1]