# Last updated: 10/21/2026, 9:59:31 PM
1class Solution:
2    def convertToBase7(self, num: int) -> str:
3        if num == 0:
4            return "0"
5        a = ''
6        sign = 0
7        if num < 0:
8            sign = '-'
9        else:
10            sign = None
11        num = abs(num)
12        while num > 0:
13            x = str(num % 7)
14            num = num // 7
15            a = x + a
16        if sign:
17            return sign + a
18        return a