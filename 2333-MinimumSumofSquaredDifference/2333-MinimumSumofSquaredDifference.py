# Last updated: 10/10/2026, 6:04:56 PM
1
2class Solution:
3    def minSumSquareDiff(self, nums1, nums2, k1, k2):
4        n = len(nums1)
5        k = k1 + k2
6        diff = [0] * n
7        largest = 0
8        sum_diff = 0
9
10        for i in range(n):
11            diff[i] = abs(nums1[i] - nums2[i])
12            largest = max(largest, diff[i])
13            sum_diff += diff[i]
14
15        if sum_diff <= k:
16            return 0
17
18        freq = [0] * (largest + 1)
19
20        for value in diff:
21            freq[value] += 1
22
23        for i in range(largest, 0, -1):
24            if k == 0:
25                break
26
27            if freq[i] == 0:
28                continue
29
30            if k >= freq[i]:
31                k -= freq[i]
32                freq[i - 1] += freq[i]
33                freq[i] = 0
34            else:
35                freq[i - 1] += k
36                freq[i] -= k
37                k = 0
38
39        result = 0
40
41        for i in range(largest + 1):
42            result += freq[i] * i * i
43
44        return result