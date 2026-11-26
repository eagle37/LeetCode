# Last updated: 11/26/2026, 10:04:38 AM
1class Solution:
2    def smallestUniqueSubarray(self, nums: list[int]) -> int:
3        n = len(nums)
4        names = [nums]  # names[k][i] same for equal windows nums[i:i + 2**k]
5        for k in range(n.bit_length() - 1):  # blocks of 2, 4, 8, ... while they fit
6            ids = {}  # pair of halves -> number of the whole window
7            names.append([ids.setdefault(pair, len(ids)) for pair in zip(names[k], names[k][2 ** k:])])
8
9        def found(length):  # is some window of this length unique?
10            k = length.bit_length() - 1  # its first 2**k elements and its last 2**k cover it
11            return 1 in Counter(zip(names[k], names[k][length - 2 ** k:])).values()
12
13        return bisect_left(range(1, n), True, key=found) + 1