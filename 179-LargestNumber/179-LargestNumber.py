# Last updated: 9/9/2026, 10:37:45 PM
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = [str(x) for x in nums]

        for i in range(1, len(nums)):
            curr = nums[i]
            j = i - 1

            while j >= 0 and curr + nums[j] > nums[j] + curr:
                nums[j + 1] = nums[j]
                j -= 1

            nums[j + 1] = curr

        ans = ''.join(nums)

        return "0" if ans[0] == "0" else ans