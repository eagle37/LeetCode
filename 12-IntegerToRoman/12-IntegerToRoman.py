# Last updated: 8/22/2026, 7:02:23 PM
class Solution:
    def intToRoman(self, num: int) -> str:
        d = [
            (1000, "M"), (900, "CM"),
            (500, "D"), (400, "CD"),
            (100, "C"), (90, "XC"),
            (50, "L"), (40, "XL"),
            (10, "X"), (9, "IX"),
            (5, "V"), (4, "IV"),
            (1, "I")
        ]

        res = ""

        for value, symbol in d:
            while num >= value:
                res += symbol
                num -= value

        return res