class Solution:
    def findThePrefixCommonArray(self, A, B):
        n = len(A)
        ans = []
        seen = set()
        count = 0
        
        for i in range(n):
            seen.add(A[i])
            seen.add(B[i])
            count = len(set(A[:i+1]) & set(B[:i+1]))
            ans.append(count)
        
        return ans
