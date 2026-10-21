# Last updated: 10/21/2026, 9:50:19 PM
1class Solution:
2    def nextGreaterElements(self, nums: list[int]) -> list[int]:
3        l = nums + nums
4        x = []
5        for i in range(len(nums)):
6            m = nums[i]
7            for j in range(i+1, len(l)):
8                if m < l[j]:
9                    m = l[j]
10                    break
11            if m == nums[i]:
12                x.append(-1)
13            else:
14                x.append(m)
15        return x