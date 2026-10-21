# Last updated: 10/21/2026, 9:32:09 PM
class Solution:
    def find132pattern(self, nums: list[int]) -> bool:
        s3 = float("-inf")
        l = []
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < s3:
                return True
            else:
                while len(l) > 0 and nums[i] > l[-1]:
                    s3 = l[-1]
                    l.pop()
                l.append(nums[i])
        return False