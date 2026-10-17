# Last updated: 10/17/2026, 5:30:28 PM
1class Solution:
2    def findComplement(self, num: int) -> int:
3        bit_length = num.bit_length()
4        
5        mask = (1 << bit_length) - 1
6        
7        return num ^ mask