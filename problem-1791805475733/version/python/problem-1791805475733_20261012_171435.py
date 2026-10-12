# Last updated: 10/12/2026, 5:14:35 PM
1class Solution:
2    def find132pattern(self, nums: list[int]) -> bool:
3        s3 = float("-inf")
4        l = []
5        for i in range(len(nums)-1, -1, -1):
6            if nums[i] < s3:
7                return True
8            else:
9                while len(l) > 0 and nums[i] > l[-1]:
10                    s3 = l[-1]
11                    l.pop()
12                l.append(nums[i])
13        return False