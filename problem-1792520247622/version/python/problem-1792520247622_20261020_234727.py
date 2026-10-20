# Last updated: 10/20/2026, 11:47:27 PM
1class Solution:
2    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
3        ans = []
4
5        for x in nums1:
6            idx = nums2.index(x)
7            greater = -1
8
9            for i in range(idx + 1, len(nums2)):
10                if nums2[i] > x:
11                    greater = nums2[i]
12                    break
13
14            ans.append(greater)
15
16        return ans