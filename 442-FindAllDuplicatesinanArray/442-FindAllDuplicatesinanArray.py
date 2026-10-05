# Last updated: 10/5/2026, 10:57:40 PM
1class Solution:
2    def findDuplicates(self, nums: List[int]) -> List[int]:
3        ans =[]
4        n=len(nums)
5        for x in nums:
6            x = abs(x)
7            if nums[x-1]<0:
8                ans.append(x)
9            nums[x-1] *= -1
10        return ans