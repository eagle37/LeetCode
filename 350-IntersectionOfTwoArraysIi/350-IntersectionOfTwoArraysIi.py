# Last updated: 8/15/2026, 4:30:43 PM
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = []
        for i in nums1:
            if i in nums2:
                l.append(i)
                nums2.remove(i)
        return l