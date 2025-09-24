class Solution:
    def checkValid(self, matrix):
        n = len(matrix)
        for i in range(n):
            row = set(matrix[i])
            col = set(matrix[j][i] for j in range(n))
            if row != set(range(1, n + 1)) or col != set(range(1, n + 1)):
                return False
        return True     
