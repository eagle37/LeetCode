# Last updated: 10/17/2026, 5:22:58 PM
1class Solution:
2    def validIPAddress(self, s: str) -> str:
3        return (fullmatch(r'\:'.join([r'[a-fA-F\d]{1,4}']*8),s) and 'IPv6' or
4            fullmatch(r'\.'.join([r'(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)']*4),s) and 'IPv4'
5                 or 'Neither')