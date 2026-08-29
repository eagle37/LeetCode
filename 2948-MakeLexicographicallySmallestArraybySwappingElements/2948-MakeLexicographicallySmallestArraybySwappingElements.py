# Last updated: 8/29/2026, 8:14:31 PM
class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups=[]
        cur=[]
        d = {}
        for x in sorted(nums):
            if not cur or x-cur[-1] <= limit:
                cur.append(x)
            else:
                groups.append(cur.copy())
                cur = [x]
            d[x] = len(groups)

        groups.append(cur.copy())
        groups = [l[::-1] for l in groups]

        return [groups[d[x]].pop() for x in nums]
        