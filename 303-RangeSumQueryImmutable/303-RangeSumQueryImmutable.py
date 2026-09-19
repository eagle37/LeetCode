# Last updated: 9/19/2026, 3:57:22 PM
class NumArray:

    def __init__(self, nums: list[int]):
        self.nums = nums

    def sumRange(self, left: int, right: int) -> int:
        x = 0
        for i in range(left, right+1):
            x += self.nums[i]
        return x


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)