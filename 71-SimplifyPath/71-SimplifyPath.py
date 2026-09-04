# Last updated: 9/4/2026, 4:11:42 PM
1class Solution:
2    def search(self, nums: List[int], target: int) -> bool:
3
4        left = 0
5        right = len(nums) - 1
6
7        while left <= right:
8
9            mid = (left + right) // 2
10
11            if nums[mid] == target:
12                return True
13
14            if nums[left] == nums[mid] == nums[right]:
15                left += 1
16                right -= 1
17
18            elif nums[left] <= nums[mid]:
19
20                if nums[left] <= target < nums[mid]:
21                    right = mid - 1
22                else:
23                    left = mid + 1
24
25            else:
26
27                if nums[mid] < target <= nums[right]:
28                    left = mid + 1
29                else:
30                    right = mid - 1
31
32        return False