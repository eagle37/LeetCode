# Last updated: 10/21/2026, 9:31:36 PM
class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        stack = []
        d = {}

        for x in nums2:
            while stack and stack[-1] < x:
                d[stack.pop()] = x
            stack.append(x)

        for x in stack:
            d[x] = -1

        return [d[x] for x in nums1]