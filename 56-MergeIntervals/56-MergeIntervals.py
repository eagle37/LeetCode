# Last updated: 9/4/2026, 3:24:22 PM
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        merge = [intervals[0]]
        for i in intervals[1:]:
            last = merge[-1]
            if i[0] <= last[1]:
                end = max(i[1], last[1])
                merge.pop()
                merge.append([last[0], end])
            else:
                merge.append(i)
        return merge