# Last updated: 8/23/2026, 6:30:13 PM
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        seen = set()
        nums.sort()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                l, r = j+1, len(nums)-1
                while l < r:
                    if nums[l] + nums[r] < target - nums[i] - nums[j]:
                        l += 1
                    elif nums[l] + nums[r] > target - nums[i] - nums[j]:
                        r -= 1
                    elif nums[l] + nums[r] == target - nums[i] - nums[j]:
                        x = (nums[i], nums[j], nums[l], nums[r])
                        if x not in seen:
                            seen.add(x)
                            ans.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
        return ans