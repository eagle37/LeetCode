# Last updated: 8/22/2026, 7:00:04 PM
1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        nums.sort()
4        li = []
5
6        for i in range(len(nums) - 2):
7            if i > 0 and nums[i] == nums[i - 1]:
8                continue
9
10            l = i + 1
11            r = len(nums) - 1
12
13            while l < r:
14                total = nums[i] + nums[l] + nums[r]
15
16                if total == 0:
17                    li.append([nums[i], nums[l], nums[r]])
18                    l += 1
19                    r -= 1
20
21                    while l < r and nums[l] == nums[l - 1]:
22                        l += 1
23
24                    while l < r and nums[r] == nums[r + 1]:
25                        r -= 1
26
27                elif total < 0:
28                    l += 1
29                else:
30                    r -= 1
31
32        return li