# Last updated: 8/15/2026, 4:30:02 PM
class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"

        hex_chars = "0123456789abcdef"
        res = ""
        num &= 0xffffffff

        while num:
            res = hex_chars[num % 16] + res
            num //= 16

        return res