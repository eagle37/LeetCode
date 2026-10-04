# Last updated: 10/4/2026, 10:04:11 PM
1class Solution:
2    def findNthDigit(self, n: int) -> int:
3        digit_in_num = 1
4        start = 1
5        end = 9
6
7        while n > digit_in_num * end:
8            n -= digit_in_num * end
9            digit_in_num += 1
10            start *= 10
11            end *= 10
12
13        num = start + (n - 1) // digit_in_num
14        return int(str(num)[(n - 1) % digit_in_num])
15        