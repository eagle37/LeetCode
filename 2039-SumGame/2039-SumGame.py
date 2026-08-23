# Last updated: 8/23/2026, 6:29:18 PM
class Solution:
    def sumGame(self, num: str) -> bool:
        ql, qr, diff = 0, 0, 0
        n = len(num)
        half = n // 2
        for i in range(n):
            if i < half:
                if num[i] == '?':
                    ql += 1
                else:
                    diff += int(num[i])
            else:
                if num[i] == '?':
                    qr += 1
                else:
                    diff -= int(num[i])
        if (ql+qr) % 2 != 0:
            return True
        return diff != 9 * (qr-ql) // 2