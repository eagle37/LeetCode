# Last updated: 8/15/2026, 4:32:28 PM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = int("".join(map(str,digits)))
        n += 1
        return [int(d) for d in str(n)]