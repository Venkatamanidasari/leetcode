class Solution:
    def transpose(self, matrix):
        return list(map(list, zip(*matrix)))

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(Solution().transpose(matrix))  # Output: [[1  
