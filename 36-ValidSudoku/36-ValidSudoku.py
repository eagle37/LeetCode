# Last updated: 8/27/2026, 3:16:13 PM
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows = [[] for _ in range(9)]
        # cols = [[] for _ in range(9)]
        # box = [[] for _ in range(9)]
        # go through each cell in board, add the num to each the row, col, box it is in, if same num appear in the these, return Flase
        
        rows = [[] for _ in range(len(board))]
        cols = [[] for _ in range(len(board[0]))]
        boxes = [[] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]
                box = (r // 3) * 3 + c // 3
                
                if num == ".":
                    continue
                elif num in rows[r] or num in cols[c] or num in boxes[box]:
                    return False
                
                else:
                    rows[r].append(num)
                    cols[c].append(num)
                    boxes[box].append(num)
        
        return True