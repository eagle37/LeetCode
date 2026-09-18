# Last updated: 9/19/2026, 12:41:44 AM
1class NumArray:
2
3    def __init__(self, nums: list[int]):
4        self.nums = nums
5
6    def sumRange(self, left: int, right: int) -> int:
7        x = 0
8        for i in range(left, right+1):
9            x += self.nums[i]
10        return x
11
12
13# Your NumArray object will be instantiated and called as such:
14# obj = NumArray(nums)
15# param_1 = obj.sumRange(left,right)