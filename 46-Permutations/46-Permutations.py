# Last updated: 8/29/2026, 8:39:24 PM
1import numpy as np
2class Solution:
3    def rotate(self, matrix: List[List[int]]) -> None:
4        """
5        Do not return anything, modify matrix in-place instead.
6        """
7        arr = np.array(matrix)
8        arr = np.rot90(arr, k=-1)
9        matrix[:] = arr.tolist()