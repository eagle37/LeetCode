# Last updated: 9/5/2026, 5:29:11 PM
1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        numset = set(nums)
4        longest = 0
5        for n in numset:
6            if n - 1 not in numset:
7                length = 1
8                while n + length in numset:
9                    length += 1
10                longest = max(longest, length)
11        return longest