# Last updated: 9/5/2026, 5:01:05 PM
1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3
4        ans = [[1]]
5
6        for i in range(1, numRows):
7
8            prev = ans[-1]
9            row = [1]
10
11            for j in range(1, i):
12                row.append(prev[j-1] + prev[j])
13
14            row.append(1)
15
16            ans.append(row)
17
18        return ans