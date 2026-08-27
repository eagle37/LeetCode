# Last updated: 8/27/2026, 3:15:48 PM
1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        row = [set() for _ in range(9)]
4        col = [set() for _ in range(9)]
5        boxes  = [set() for _ in range(9)]
6
7        for r in range(9):
8            for c in range(9):
9
10                num = board[r][c]
11                if num == '.':
12                    continue
13                box = (r//3)*3 + (c//3)
14
15                if num in row[r]:
16                    return False
17                if num in col[c]:
18                    return False
19                if num in boxes[box]:
20                    return False
21                
22                row[r].add(num)
23                col[c].add(num)
24                boxes[box].add(num)
25
26        return True