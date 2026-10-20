# Last updated: 10/20/2026, 11:48:40 PM
1class Solution:
2    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
3        stack = []
4        d = {}
5
6        for x in nums2:
7            while stack and stack[-1] < x:
8                d[stack.pop()] = x
9            stack.append(x)
10
11        for x in stack:
12            d[x] = -1
13
14        return [d[x] for x in nums1]