# Last updated: 9/5/2026, 5:01:31 PM
1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        i = m-1
7        j = n-1 
8        k = m+n-1
9
10        while j>=0:
11            if i<0 or nums1[i] < nums2[j]:
12                nums1[k] = nums2[j]
13                j-=1
14                k-=1
15            else:
16                nums1[k] = nums1[i]
17                i-=1
18                k-=1
19