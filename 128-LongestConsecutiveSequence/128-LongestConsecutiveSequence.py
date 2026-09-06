# Last updated: 9/6/2026, 10:48:17 PM
1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3
4        total = 0
5        curr = 0
6        start = 0
7
8        for i in range(len(gas)):
9            diff = gas[i] - cost[i]
10
11            total += diff
12            curr += diff
13
14            if curr < 0:
15                start = i + 1
16                curr = 0
17
18        if total < 0:
19            return -1
20
21        return start