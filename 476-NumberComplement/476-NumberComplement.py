# Last updated: 10/21/2026, 9:31:57 PM
class Solution:
    def findComplement(self, num: int) -> int:
        bit_length = num.bit_length()
        
        mask = (1 << bit_length) - 1
        
        return num ^ mask