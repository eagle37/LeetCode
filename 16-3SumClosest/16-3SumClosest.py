# Last updated: 8/23/2026, 6:23:06 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        ans = []
4        nums.sort()
5        for i in range(len(nums)):
6            for j in range(i+1, len(nums)):
7                l, r = j+1, len(nums)-1
8                while l < r:
9                    if nums[l] + nums[r] < target - nums[i] - nums[j]:
10                        l += 1
11                    elif nums[l] + nums[r] > target - nums[i] - nums[j]:
12                        r -= 1
13                    elif nums[l] + nums[r] == target - nums[i] - nums[j]:
14                        if [nums[i], nums[j], nums[l], nums[r]] not in ans:
15                            ans.append([nums[i], nums[j], nums[l], nums[r]])
16                            l += 1
17                            r -= 1
18                        else:
19                            l += 1
20                            r -= 1
21        return ans