from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        s = 0
        j = n - 1
        
        for i in range(n):
            if i != j:
                s += mat[i][i] + mat[i][j]  # primary + secondary diagonal
            else:
                s += mat[i][i]  # center element (only once)
            j -= 1
        
        return s
        
