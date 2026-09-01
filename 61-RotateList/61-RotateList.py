# Last updated: 9/1/2026, 11:21:58 PM
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        if digits[-1] < 9:
4            digits[-1] += 1
5            return digits
6        s = 0
7        k = 1
8        for i in digits[::-1]:
9            s += i * k
10            k *= 10
11        s += 1
12        j = -1
13        li = []
14        while s > 0:
15            d = s % 10
16            s = s // 10
17            li.insert(j, d)
18            j -= 1
19        return li