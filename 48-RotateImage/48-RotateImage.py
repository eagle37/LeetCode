# Last updated: 9/4/2026, 3:24:31 PM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n= len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]
            
        for row in matrix:
            row.reverse()
