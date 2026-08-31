# Last updated: 8/31/2026, 10:43:08 PM
1class Solution:
2    def getPermutation(self, n: int, k: int) -> str:
3
4        nums = [str(i) for i in range(1, n + 1)]
5
6        def fact(x):
7            if x <= 1:
8                return 1
9            return x * fact(x - 1)
10
11        def solve(nums, k):
12            if len(nums) == 1:
13                return nums[0]
14
15            block = fact(len(nums) - 1)
16
17            index = (k - 1) // block
18            chosen = nums.pop(index)
19
20            k = (k - 1) % block + 1
21
22            return chosen + solve(nums, k)
23
24        return solve(nums, k)