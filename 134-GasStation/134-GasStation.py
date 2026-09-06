# Last updated: 9/6/2026, 11:53:25 PM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total = 0
        curr = 0
        start = 0

        for i in range(len(gas)):
            diff = gas[i] - cost[i]

            total += diff
            curr += diff

            if curr < 0:
                start = i + 1
                curr = 0

        if total < 0:
            return -1

        return start