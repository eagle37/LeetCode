# Last updated: 8/31/2026, 10:30:51 PM
1class Solution:
2    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
3
4        critical = []
5
6        prev = head
7        curr = head.next
8        nxt = curr.next
9
10        i = 1
11
12        while nxt:
13            if ((curr.val > prev.val and curr.val > nxt.val) or
14                (curr.val < prev.val and curr.val < nxt.val)):
15
16                critical.append(i)
17
18            prev = curr
19            curr = nxt
20            nxt = nxt.next
21            i += 1
22
23        if len(critical) < 2:
24            return [-1, -1]
25
26        max_dist = critical[-1] - critical[0]
27
28        min_dist = float('inf')
29
30        for i in range(1, len(critical)):
31            min_dist = min(
32                min_dist,
33                critical[i] - critical[i - 1]
34            )
35
36        return [min_dist, max_dist]