# Last updated: 9/4/2026, 3:32:50 PM
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        critical = []

        prev = head
        curr = head.next
        nxt = curr.next

        i = 1

        while nxt:
            if ((curr.val > prev.val and curr.val > nxt.val) or
                (curr.val < prev.val and curr.val < nxt.val)):

                critical.append(i)

            prev = curr
            curr = nxt
            nxt = nxt.next
            i += 1

        if len(critical) < 2:
            return [-1, -1]

        max_dist = critical[-1] - critical[0]

        min_dist = float('inf')

        for i in range(1, len(critical)):
            min_dist = min(
                min_dist,
                critical[i] - critical[i - 1]
            )

        return [min_dist, max_dist]