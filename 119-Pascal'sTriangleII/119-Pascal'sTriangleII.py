# Last updated: 9/5/2026, 4:58:16 PM
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        triangle = []
        for i in range(rowIndex+1):
            a = [1]*(i+1)
            for j in range(1,i):
                a[j] = triangle[i-1][j-1] + triangle[i-1][j]


            triangle.append(a)

        return triangle[rowIndex]