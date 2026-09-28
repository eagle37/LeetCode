# Last updated: 9/29/2026, 12:15:38 AM
1class Solution:
2    def isHappy(self, n: int) -> bool:
3        seen = set()
4        while n != 1:
5            if n in seen:
6                return False
7            seen.add(n)
8            
9            new_n = 0
10            while n > 0:
11                digit = n % 10
12                new_n += digit * digit
13                n //= 10
14            n = new_n
15        return True