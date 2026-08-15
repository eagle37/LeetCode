# Last updated: 8/15/2026, 4:30:45 PM
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a,b = set(nums1), set(nums2)
        return list(a&b)