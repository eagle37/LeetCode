# Last updated: 10/17/2026, 5:07:17 PM
1class Solution:
2    def minSwaps(self, nums: List[int]) -> int:
3        digit_sum = lambda x: sum(map(int, str(x)))
4        rank = {x: k for k, x in enumerate(sorted(nums, key=lambda x: (digit_sum(x), x)))}
5        home = [rank[x] for x in nums]
6
7        swaps = 0
8        for i in range(len(home)):
9            while home[i] != i:
10                j = home[i]
11                home[i], home[j] = home[j], home[i]
12                swaps += 1
13
14        return swaps