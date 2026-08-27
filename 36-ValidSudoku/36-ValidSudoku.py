# Last updated: 8/27/2026, 3:37:14 PM
1class Solution:
2    def solveSudoku(self, board: List[List[str]]) -> None:
3
4        rows = [set() for _ in range(9)]
5        cols = [set() for _ in range(9)]
6        boxes = [set() for _ in range(9)]
7
8        for r in range(9):
9            for c in range(9):
10
11                if board[r][c] != '.':
12                    num = board[r][c]
13                    box = (r // 3) * 3 + (c // 3)
14
15                    rows[r].add(num)
16                    cols[c].add(num)
17                    boxes[box].add(num)
18
19        def backtrack():
20
21            for r in range(9):
22                for c in range(9):
23
24                    if board[r][c] == '.':
25
26                        box = (r // 3) * 3 + (c // 3)
27
28                        for num in "123456789":
29
30                            if (num not in rows[r] and
31                                num not in cols[c] and
32                                num not in boxes[box]):
33
34                                board[r][c] = num
35                                rows[r].add(num)
36                                cols[c].add(num)
37                                boxes[box].add(num)
38
39                                if backtrack():
40                                    return True
41
42                                board[r][c] = '.'
43                                rows[r].remove(num)
44                                cols[c].remove(num)
45                                boxes[box].remove(num)
46
47                        return False
48
49            return True
50
51        backtrack()