# Last updated: 8/15/2026, 4:32:25 PM
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a,2)+int(b,2))[2:]