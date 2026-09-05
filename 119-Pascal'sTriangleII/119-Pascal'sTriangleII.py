# Last updated: 9/5/2026, 4:57:33 PM
1class Solution:
2    def getRow(self, rowIndex: int) -> List[int]:
3        ans = [1]
4
5        for i in range(1, rowIndex+1):
6
7            prev = ans
8            row = [1]
9
10            for j in range(1, i):
11                row.append(prev[j-1] + prev[j])
12
13            row.append(1)
14
15            ans = row
16
17        return ans