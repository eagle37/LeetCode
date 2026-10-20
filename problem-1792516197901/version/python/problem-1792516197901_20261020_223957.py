# Last updated: 10/20/2026, 10:39:57 PM
1class Solution:
2    def func(self, idx: int, nums: list[int], a: list[int], ans: set) -> None:
3        n = len(nums)
4        if idx >= n:
5            if len(a) >= 2:
6                ans.add(tuple(a))
7            return
8        if not a or nums[idx] >= a[-1]:
9            a.append(nums[idx])
10            self.func(idx + 1, nums, a, ans)
11            a.pop()
12        self.func(idx + 1, nums, a, ans)
13
14    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
15        temp = []
16        ans = set()
17        self.func(0, nums, temp, ans)
18        return [list(t) for t in sorted(ans)]