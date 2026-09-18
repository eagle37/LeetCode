# Last updated: 9/19/2026, 12:26:01 AM
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution(object):
5    def firstBadVersion(self, n):
6        left, right = 1, n
7        while left < right:
8            mid = (left + right) // 2
9            if isBadVersion(mid):
10                right = mid
11            else:
12                left = mid + 1
13        return left