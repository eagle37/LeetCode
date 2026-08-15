# Last updated: 8/15/2026, 10:50:30 PM
1class Solution:
2    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
3        _ = nums1 + nums2
4        _.sort()
5        ____ = 0
6        if len(_) % 2 == 0:
7            __, ___ = _[(len(_)//2)-1], _[(len(_)//2)]
8            ____ = (__ + ___) / 2
9        else:
10            ____ = _[(len(_) // 2)]
11        return ____