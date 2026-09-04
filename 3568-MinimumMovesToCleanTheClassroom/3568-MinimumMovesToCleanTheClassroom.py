# Last updated: 9/4/2026, 3:32:34 PM
from collections import deque

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m = len(classroom)
        n = len(classroom[0])

        litter_id = {}
        sr = sc = 0
        count = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c

                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = count
                    count += 1

        if count == 0:
            return 0

        full_mask = (1 << count) - 1

        best = [
            [[-1] * (1 << count) for _ in range(n)]
            for _ in range(m)
        ]

        q = deque([(sr, sc, energy, 0)])

        best[sr][sc][0] = energy

        moves = 0

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]

        while q:

            for _ in range(len(q)):

                r, c, e, mask = q.popleft()

                if mask == full_mask:
                    return moves

                if e == 0:
                    continue

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if not (0 <= nr < m and 0 <= nc < n):
                        continue

                    if classroom[nr][nc] == 'X':
                        continue

                    ne = e - 1

                    if classroom[nr][nc] == 'R':
                        ne = energy

                    nmask = mask

                    if classroom[nr][nc] == 'L':
                        idx = litter_id[(nr, nc)]
                        nmask |= (1 << idx)

                    if ne <= best[nr][nc][nmask]:
                        continue

                    best[nr][nc][nmask] = ne

                    q.append((nr, nc, ne, nmask))

            moves += 1

        return -1