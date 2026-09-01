# Last updated: 9/1/2026, 10:56:01 PM
1from collections import deque
2
3class Solution:
4    def minMoves(self, classroom: List[str], energy: int) -> int:
5
6        m = len(classroom)
7        n = len(classroom[0])
8
9        litter_id = {}
10        sr = sc = 0
11        count = 0
12
13        for r in range(m):
14            for c in range(n):
15                if classroom[r][c] == 'S':
16                    sr, sc = r, c
17
18                elif classroom[r][c] == 'L':
19                    litter_id[(r, c)] = count
20                    count += 1
21
22        if count == 0:
23            return 0
24
25        full_mask = (1 << count) - 1
26
27        best = [
28            [[-1] * (1 << count) for _ in range(n)]
29            for _ in range(m)
30        ]
31
32        q = deque([(sr, sc, energy, 0)])
33
34        best[sr][sc][0] = energy
35
36        moves = 0
37
38        directions = [
39            (-1, 0),
40            (1, 0),
41            (0, -1),
42            (0, 1)
43        ]
44
45        while q:
46
47            for _ in range(len(q)):
48
49                r, c, e, mask = q.popleft()
50
51                if mask == full_mask:
52                    return moves
53
54                if e == 0:
55                    continue
56
57                for dr, dc in directions:
58
59                    nr = r + dr
60                    nc = c + dc
61
62                    if not (0 <= nr < m and 0 <= nc < n):
63                        continue
64
65                    if classroom[nr][nc] == 'X':
66                        continue
67
68                    ne = e - 1
69
70                    if classroom[nr][nc] == 'R':
71                        ne = energy
72
73                    nmask = mask
74
75                    if classroom[nr][nc] == 'L':
76                        idx = litter_id[(nr, nc)]
77                        nmask |= (1 << idx)
78
79                    if ne <= best[nr][nc][nmask]:
80                        continue
81
82                    best[nr][nc][nmask] = ne
83
84                    q.append((nr, nc, ne, nmask))
85
86            moves += 1
87
88        return -1