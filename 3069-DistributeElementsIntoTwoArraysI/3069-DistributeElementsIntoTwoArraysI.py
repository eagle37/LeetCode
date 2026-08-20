# Last updated: 8/20/2026, 4:22:52 PM
1class Solution:
2    def resultArray(self, nums: List[int]) -> List[int]:
3        if len(nums) < 2:
4            return nums
5        arr1 = [nums[0]]
6        arr2 = [nums[1]]
7        for i in range(2, len(nums)):
8            if arr1[-1] > arr2[-1]:
9                arr1.append(nums[i])
10            else:
11                arr2.append(nums[i])
12        return arr1 + arr2