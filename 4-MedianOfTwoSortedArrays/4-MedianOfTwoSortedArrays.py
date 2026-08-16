# Last updated: 8/16/2026, 11:45:05 PM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        _ = nums1 + nums2
        _.sort()
        ____ = 0
        if len(_) % 2 == 0:
            __, ___ = _[(len(_)//2)-1], _[(len(_)//2)]
            ____ = (__ + ___) / 2
        else:
            ____ = _[(len(_) // 2)]
        return ____