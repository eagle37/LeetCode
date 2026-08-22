# Last updated: 8/22/2026, 6:01:47 PM
1class Solution:
2    def intToRoman(self, num: int) -> str:
3        d = [
4            (1000, "M"), (900, "CM"),
5            (500, "D"), (400, "CD"),
6            (100, "C"), (90, "XC"),
7            (50, "L"), (40, "XL"),
8            (10, "X"), (9, "IX"),
9            (5, "V"), (4, "IV"),
10            (1, "I")
11        ]
12
13        res = ""
14
15        for value, symbol in d:
16            while num >= value:
17                res += symbol
18                num -= value
19
20        return res