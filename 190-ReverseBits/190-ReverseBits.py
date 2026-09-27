# Last updated: 9/27/2026, 7:09:41 PM
class Solution:
    def reverseBits(self, n: int) -> int:
        k = bin(n)
        j = ""
        z = len(k)
        for i in range(z):
            if i == 1:
                continue
            j += k[i]
        z = len(j)
        ok = 32-z
        l = "0"*ok
        j = l+j
        i = 0
        ans = 0
        for _ in range(32):
            ans =  ans + ((int(j[_]) * (2**i)))
            i += 1
        return ans