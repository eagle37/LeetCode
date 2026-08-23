# Last updated: 8/23/2026, 6:27:24 PM
1class Solution:
2    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
3        ans = []
4        seen = set()
5        nums.sort()
6        for i in range(len(nums)):
7            for j in range(i+1, len(nums)):
8                l, r = j+1, len(nums)-1
9                while l < r:
10                    if nums[l] + nums[r] < target - nums[i] - nums[j]:
11                        l += 1
12                    elif nums[l] + nums[r] > target - nums[i] - nums[j]:
13                        r -= 1
14                    elif nums[l] + nums[r] == target - nums[i] - nums[j]:
15                        x = (nums[i], nums[j], nums[l], nums[r])
16                        if x not in seen:
17                            seen.add(x)
18                            ans.append([nums[i], nums[j], nums[l], nums[r]])
19                        l += 1
20                        r -= 1
21        return ans