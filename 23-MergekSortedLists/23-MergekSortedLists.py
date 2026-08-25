# Last updated: 8/25/2026, 11:58:20 PM
1class Solution:
2    def searchRange(self, nums: List[int], target: int) -> List[int]:
3
4        def first_position():
5            left = 0
6            right = len(nums) - 1
7            ans = -1
8
9            while left <= right:
10                mid = left + (right - left) // 2
11
12                if nums[mid] == target:
13                    ans = mid
14                    right = mid - 1
15
16                elif nums[mid] < target:
17                    left = mid + 1
18
19                else:
20                    right = mid - 1
21
22            return ans
23
24        def last_position():
25            left = 0
26            right = len(nums) - 1
27            ans = -1
28
29            while left <= right:
30                mid = left + (right - left) // 2
31
32                if nums[mid] == target:
33                    ans = mid
34                    left = mid + 1
35
36                elif nums[mid] < target:
37                    left = mid + 1
38
39                else:
40                    right = mid - 1
41
42            return ans
43
44        return [first_position(), last_position()]