# Last updated: 8/29/2026, 8:14:16 PM
1class Solution:
2    def lexicographicallySmallestArray(self, nums, limit):
3        n = len(nums)
4        arr = sorted((num, i) for i, num in enumerate(nums))
5
6        i = 0
7
8        while i < n:
9            j = i
10
11            while j + 1 < n and arr[j + 1][0] - arr[j][0] <= limit:
12                j += 1
13
14            indices = sorted(arr[k][1] for k in range(i, j + 1))
15
16            for k in range(len(indices)):
17                nums[indices[k]] = arr[i + k][0]
18
19            i = j + 1
20
21        return nums