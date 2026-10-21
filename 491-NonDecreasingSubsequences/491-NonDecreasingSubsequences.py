# Last updated: 10/21/2026, 9:31:46 PM
class Solution:
    def func(self, idx: int, nums: list[int], a: list[int], ans: set) -> None:
        n = len(nums)
        if idx >= n:
            if len(a) >= 2:
                ans.add(tuple(a))
            return
        if not a or nums[idx] >= a[-1]:
            a.append(nums[idx])
            self.func(idx + 1, nums, a, ans)
            a.pop()
        self.func(idx + 1, nums, a, ans)

    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        temp = []
        ans = set()
        self.func(0, nums, temp, ans)
        return [list(t) for t in sorted(ans)]