# Last updated: 9/2/2026, 11:18:36 PM
1class Solution:
2    def sortColors(self, nums: List[int]) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        low = 0
7        mid = 0
8        high = len(nums) - 1
9
10        while mid <= high:
11
12            if nums[mid] == 0:
13                nums[low], nums[mid] = nums[mid], nums[low]
14                low += 1
15                mid += 1
16
17            elif nums[mid] == 1:
18                mid += 1
19
20            else:
21                nums[mid], nums[high] = nums[high], nums[mid]
22                high -= 1