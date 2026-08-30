# Last updated: 8/30/2026, 4:18:43 PM
1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort()
4        merge = [intervals[0]]
5        for i in intervals[1:]:
6            last = merge[-1]
7            if i[0] <= last[1]:
8                end = max(i[1], last[1])
9                merge.pop()
10                merge.append([last[0], end])
11            else:
12                merge.append(i)
13        return merge