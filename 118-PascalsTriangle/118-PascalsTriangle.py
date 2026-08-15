# Last updated: 8/15/2026, 4:32:13 PM
class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i + 1)
            
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]

            triangle.append(row)

        return triangle